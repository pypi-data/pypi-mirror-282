import json
from functools import lru_cache, partial
from typing import Callable, List, Union

from promptflow import tool

from ..utils import RankerType
from ..rankers import api_rerank, bm25_rerank, ssf_rerank


@lru_cache(maxsize=32)
def _get_rerank_func(
    ranker_parameters: Union[dict, str],
) -> Callable[[str, List[List[dict]]], List[dict]]:

    if isinstance(ranker_parameters, str):
        ranker_parameters = json.loads(ranker_parameters)

    ranker_type = ranker_parameters.get("ranker_type")

    if ranker_type == RankerType.BM25:
        return bm25_rerank

    if ranker_type == RankerType.ScaledScoreFusion:
        ssf_rank_constant = ranker_parameters.get("ssf_rank_constant")
        if ssf_rank_constant:
            return partial(ssf_rerank, ssf_rank_constant=ssf_rank_constant)
        else:
            return ssf_rerank

    if ranker_type == RankerType.ApiKeyConnection:
        return partial(
            api_rerank,
            api_base=ranker_parameters.get("api_base"),
            api_key=ranker_parameters.get("api_key"),
        )

    if ranker_type == RankerType.ServerlessDeployment:
        return partial(
            api_rerank,
            api_base=ranker_parameters.get("api_base"),
            api_key=ranker_parameters.get("api_key"),
        )

    raise ValueError()


@tool
def rerank(
    ranker_parameters: Union[str, dict],
    query: str,
    result_groups: Union[List[dict], List[List[dict]]],
    top_k: int,
) -> List[dict]:
    if isinstance(result_groups, list):
        if isinstance(result_groups[0], dict):
            result_groups = [result_groups]
        elif isinstance(result_groups[0], list) and isinstance(result_groups[0][0], dict):
            pass
        else:
            raise ValueError()
    else:
        raise ValueError()

    rerank_func = _get_rerank_func(ranker_parameters)
    return rerank_func(query=query, result_groups=result_groups, top_k=top_k)
