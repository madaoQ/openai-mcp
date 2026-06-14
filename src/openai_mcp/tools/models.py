# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Model listing tools for OpenAI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from openai_mcp.request import request
from openai_mcp.types import JSONObject


@tool(
    description="List all available OpenAI models.",
    tags=["models", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def openai_list_models() -> JSONObject:
    """List all available OpenAI models.

    Returns:
        List of models with their properties.

    Raises:
        RuntimeError: If the API request fails.

    """
    result = await request(HttpMethod.GET, "/models")
    return result


model_tools = [openai_list_models]