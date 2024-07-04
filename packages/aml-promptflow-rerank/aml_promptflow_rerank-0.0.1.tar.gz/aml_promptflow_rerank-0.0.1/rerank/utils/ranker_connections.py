from typing import Dict, List

from .callback import CallbackContext, tool_ui_callback
from .ranker_types import api_base_points_to_cohere, resolve_serverless_connection


@tool_ui_callback
def list_apikey_ranker_connections(context: CallbackContext) -> List[Dict[str, str]]:
    apikey_connections = context.ml_client.connections._operation.list(
        workspace_name=context.workspace_name,
        cls=lambda objs: objs,
        category="ApiKey",
        **context.ml_client.connections._scope_kwargs,
    )

    valid_apikey_connections = []
    for connection in apikey_connections:
        if connection.properties.category == "ApiKey":
            api_base, info = resolve_serverless_connection(context, connection)
            if info.get("model_type") == "rerank" or api_base_points_to_cohere(api_base):
                valid_apikey_connections.append({"value": connection.name, "display_value": connection.name})

    return valid_apikey_connections
