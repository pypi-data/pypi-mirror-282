from typing import List

import requests


def api_rerank(query: str, result_groups: List[List[dict]], top_k: int, api_base: str, api_key: str) -> List[dict]:
    if api_key is None:
        raise ValueError("An API Key is required for API-based reranker deployments.")

    flattened_results = [item for group in result_groups for item in group]
    corpus = [result["text"] for result in flattened_results]

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    json_body = {"query": query, "documents": corpus, "top_n": top_k}

    try:
        api_response = requests.post(api_base, headers=headers, json=json_body)
        api_response.raise_for_status()
        api_json = api_response.json()

        sorted_results = []
        api_response_results = api_json.get("results")
        for api_response_result in api_response_results:
            result_index = api_response_result.get("index")
            result = flattened_results[result_index]
            if "additional_fields" not in result:
                result["additional_fields"] = dict()

            result["additional_fields"]["@promptflow_vectordb.reranker_score"] = api_response_result.get(
                "relevance_score"
            )
            sorted_results.append(result)

    except Exception:
        api_json = dict()
        sorted_results = list(reversed(sorted(flattened_results, key=lambda r: r["score"])))[:top_k]

    return sorted_results
