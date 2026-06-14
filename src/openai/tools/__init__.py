# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Tool registry for openai-mcp.

Modules:
  chat       -- openai_create_response
  embed      -- openai_create_embedding
  moderate   -- openai_moderate_text
  models     -- openai_list_models
  files      -- openai_list_files, openai_upload_file
"""

from __future__ import annotations

from openai.tools.chat import chat_tools
from openai.tools.embed import embed_tools
from openai.tools.files import file_tools
from openai.tools.models import model_tools
from openai.tools.moderate import moderate_tools

openai_tools = [
    *chat_tools,
    *embed_tools,
    *moderate_tools,
    *model_tools,
    *file_tools,
]