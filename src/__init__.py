"""
OpenAI MCP Server

A Type 3 DAuth MCP server for OpenAI API.
Provides models, chat, embeddings, moderation, and file management.
"""

from .openai import create_openai_connection, openai_tools

__all__ = ["create_openai_connection", "openai_tools"]