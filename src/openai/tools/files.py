# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""File management tools for OpenAI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from openai.guards import validate_limit, validate_purpose
from openai.request import request
from openai.types import JSONObject


@tool(
    description="List files in your OpenAI organization.",
    tags=["files", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def openai_list_files(
    purpose: str | None = None,
    limit: int = 100,
) -> JSONObject:
    """List files.

    Args:
        purpose: Filter by purpose (assistants, batch, fine-tune).
        limit: Maximum number of files.

    Returns:
        List of files.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_limit(limit)
    if purpose is not None:
        validate_purpose(purpose)

    result = await request(
        HttpMethod.GET, "/files", params={"limit": limit, "purpose": purpose}
    )
    return result


@tool(
    description="Upload a file to OpenAI.",
    tags=["files", "write"],
    annotations=ToolAnnotations(readOnlyHint=False),
)
async def openai_upload_file(
    file_path: str,
    purpose: str = "assistants",
) -> JSONObject:
    """Upload a file.

    Args:
        file_path: Path to file to upload.
        purpose: Purpose (assistants, batch, fine-tune).

    Returns:
        Upload confirmation with file ID.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_purpose(purpose)

    body: JSONObject = {
        "file": file_path,
        "purpose": purpose,
    }

    result = await request(HttpMethod.POST, "/files", body)
    return result


file_tools = [openai_list_files, openai_upload_file]