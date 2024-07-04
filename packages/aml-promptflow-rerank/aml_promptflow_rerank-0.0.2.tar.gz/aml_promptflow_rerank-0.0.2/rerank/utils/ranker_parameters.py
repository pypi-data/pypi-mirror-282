import json
from typing import Any, Dict

from .callback import CallbackContext, tool_ui_callback
from .constants import RankerType
from .ranker_types import api_base_points_to_cohere, get_connection_key, resolve_serverless_connection


@tool_ui_callback
def generate_ranker_parameters(
    context: CallbackContext,
    ranker_type: str,
    api_connection: str = None,
    serverless_connection: str = None,
    ssf_rank_constant: int = None,
) -> Dict[str, Any]:
    if ranker_type == RankerType.BM25:
        ranker_config = {"ranker_type": RankerType.BM25}
    elif ranker_type == RankerType.ScaledScoreFusion:
        ranker_config = {"ranker_type": RankerType.ScaledScoreFusion, "ssf_rank_constant": ssf_rank_constant}
    elif ranker_type == RankerType.ApiKeyConnection:
        if api_connection is not None:
            ranker_config = {"ranker_type": RankerType.ApiKeyConnection}
            ranker_config.update(_fetch_ranker_config_from_connection(context, "ApiKey", api_connection))
        else:
            raise NotImplementedError("ApiKey connections require an explicit connection.")
    elif ranker_type == RankerType.ServerlessDeployment:
        if serverless_connection is not None:
            ranker_config = {"ranker_type": RankerType.ServerlessDeployment}
            ranker_config.update(_fetch_ranker_config_from_connection(context, "Serverless", serverless_connection))
        else:
            raise NotImplementedError("Serverless connections require an explicit connection.")
    else:
        raise ValueError(f"Unexpected ranker type: {ranker_type}")

    try:
        ranker_parameters = json.dumps(ranker_config)
    except Exception as e:
        raise ValueError(f"Failed to process ranker parameters with exception: { e }")

    return ranker_parameters


@tool_ui_callback
def reverse_ranker_parameters(
    context: CallbackContext,
    ranker_parameters: str,
) -> Dict[str, Any]:
    try:
        if isinstance(ranker_parameters, str):
            ranker_parameters = json.loads(ranker_parameters)
    except Exception as e:
        raise ValueError(f"Failed to process ranker parameters with exception: { e }")

    return ranker_parameters


def _fetch_ranker_config_from_connection(
    context: CallbackContext, connection_category: str, connection_name: str
) -> Dict[str, Any]:
    connections = context.ml_client.connections._operation.list(
        workspace_name=context.workspace_name,
        cls=lambda objs: objs,
        category=connection_category,
        **context.ml_client.connections._scope_kwargs,
    )

    for connection in connections:
        if connection.properties.category == connection_category and connection.name == connection_name:

            api_base, _ = resolve_serverless_connection(context, connection)
            api_key = get_connection_key(context, connection)
            if api_base_points_to_cohere(api_base):
                api_base = api_base.rstrip("/")
            return {"api_base": api_base, "api_key": api_key}

    raise ValueError(f'No connection was found with name "{connection_name}".')
