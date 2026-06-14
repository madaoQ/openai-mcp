# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""OpenAI MCP server for Dedalus.

Provides chat completions, embeddings, moderation, and file management using OpenAI API.
Credentials provided by clients at runtime via DAuth token exchange.
"""

from __future__ import annotations

from openai.config import create_openai_connection
from openai.tools import openai_tools

__all__ = ["create_openai_connection", "openai_tools"]