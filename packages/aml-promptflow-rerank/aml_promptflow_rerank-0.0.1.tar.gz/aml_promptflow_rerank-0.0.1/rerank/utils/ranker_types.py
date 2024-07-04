import re
from typing import Dict, List

from azureml.rag.utils.connections import connection_to_credential

from .callback import CallbackContext, tool_ui_callback
from .constants import RankerType


@tool_ui_callback
def list_available_ranker_types(context: CallbackContext) -> List[Dict[str, str]]:
    apikey_connections = context.ml_client.connections._operation.list(
        workspace_name=context.workspace_name,
        cls=lambda objs: objs,
        category="ApiKey",
        **context.ml_client.connections._scope_kwargs,
    )

    workspace_contains_apikey_connection = False
    for connection in apikey_connections:
        if connection.properties.category == "ApiKey":
            if workspace_contains_apikey_connection:
                continue

            api_base, info = resolve_serverless_connection(context, connection)
            if info.get("model_type") == "rerank" or api_base_points_to_cohere(api_base):
                workspace_contains_apikey_connection = True
                break

    serverless_connections = context.ml_client.connections._operation.list(
        workspace_name=context.workspace_name,
        cls=lambda objs: objs,
        category="Serverless",
        **context.ml_client.connections._scope_kwargs,
    )

    workspace_contains_serverless_connection = False
    for connection in serverless_connections:
        if connection.properties.category == "Serverless":
            if workspace_contains_serverless_connection:
                continue

            (_, info) = resolve_serverless_connection(context, connection)
            if info.get("model_type") == "rerank":
                workspace_contains_serverless_connection = True
                break

    workspace_contains_serverless_deployment = False
    try:
        auth_header = f'Bearer {context.credential.get_token("https://management.azure.com/.default").token}'
        response = context.http.get(
            f"https://management.azure.com{context.arm_id}" "/serverlessEndpoints?api-version=2024-01-01-preview",
            headers={"Authorization": auth_header},
        )
        response.raise_for_status()
        deployments = response.json()

        for deployment in deployments.get("value", []):
            (_, info) = _resolve_serverless_deployment(context, deployment)
            if info.get("model_type") == "rerank":
                workspace_contains_serverless_deployment = True
                break
    except Exception:
        # Ignore forbidden exceptions - the user may not have access to list deployments.
        if response.status_code != 403:
            raise

    ranker_types = []

    ranker_types.append({"value": RankerType.BM25, "display_value": RankerType.BM25})
    ranker_types.append({"value": RankerType.ScaledScoreFusion, "display_value": RankerType.ScaledScoreFusion})

    if workspace_contains_serverless_connection or workspace_contains_serverless_deployment:
        ranker_types.append(
            {"value": RankerType.ServerlessDeployment, "display_value": RankerType.ServerlessDeployment}
        )

    if workspace_contains_apikey_connection:
        ranker_types.append({"value": RankerType.ApiKeyConnection, "display_value": RankerType.ApiKeyConnection})

    return ranker_types


def api_base_points_to_cohere(api_base):
    # Regular expression for cohere rerank in various locations for various versions
    cohere_pattern = r"https://cohere-.*-rerank-.*-ep\..*\.inference\..*\.azure\.com/.*/rerank/?$"
    return bool(re.fullmatch(cohere_pattern, api_base))


def resolve_serverless_connection(context, connection):
    connection_info = {
        "model_type": connection.properties.metadata.get("served_model_type")
        or connection.properties.metadata.get("model_type"),
        "model_name": connection.properties.metadata.get("model_name")
        or connection.properties.metadata.get("served_model_name"),
        "provider_name": connection.properties.metadata.get("model_provider_name"),
    }

    api_base = connection.properties.target

    if any([value is None for value in connection_info.values()]):
        api_key = get_connection_key(context, connection)
        info = _get_serverless_deployment_info(context, api_base, api_key)
        return (api_base, ({key: connection_info.get(key) or info.get(key) for key in connection_info}))
    else:
        return (api_base, connection_info)


def get_connection_key(context, connection):
    auth_header = f'Bearer {context.credential.get_token("https://management.azure.com/.default").token}'
    list_secrets_response = context.http.post(
        f"https://management.azure.com{connection.id}/listSecrets?api-version=2024-01-01-preview",
        headers={"Authorization": auth_header},
    )
    api_key = connection_to_credential(list_secrets_response.json()).key
    return api_key


def _resolve_serverless_deployment(context, deployment):
    auth_header = f'Bearer {context.credential.get_token("https://management.azure.com/.default").token}'
    api_base = deployment.get("properties", {}).get("inferenceEndpoint", {}).get("uri")
    api_key = (
        context.http.post(
            f'https://management.azure.com{deployment.get("id")}/listKeys?api-version=2024-01-01-preview',
            headers={"Authorization": auth_header},
        )
        .json()
        .get("primaryKey")
    )

    info = _get_serverless_deployment_info(context, api_base, api_key)
    return (api_base, info)


def _get_serverless_deployment_info(context, api_base, api_key):
    try:
        info_response = context.http.get(f"{api_base}/info", headers={"Authorization": f"Bearer {api_key}"})
        info_response.raise_for_status()
        info_json = info_response.json()
    except Exception:
        info_json = dict()

    return {
        "model_type": info_json.get("served_model_type") or info_json.get("model_type"),
        "model_name": info_json.get("served_model_name") or info_json.get("model_name"),
        "provider_name": info_json.get("model_provider_name"),
    }
