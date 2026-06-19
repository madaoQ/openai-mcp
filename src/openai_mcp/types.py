# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for OpenAI API responses."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class ModelInfo(BaseModel):
    """OpenAI model info."""
    model_config = _FROZEN_SLOT


    id: str
    object: str | None = None
    created: int | None = None
    owned_by: str | None = None


class ModelList(BaseModel):
    """List of models."""
    model_config = _FROZEN_SLOT


    object: str | None = None
    data: list[ModelInfo] = Field(default_factory=list)


class EmbeddingItem(BaseModel):
    """Single embedding result."""
    model_config = _FROZEN_SLOT


    embedding: list[float]
    index: int | None = None
    object: str | None = None


class EmbeddingResponse(BaseModel):
    """Embedding API response."""
    model_config = _FROZEN_SLOT


    object: str | None = None
    model: str | None = None
    embeddings: list[list[float]] = Field(default_factory=list)
    usage: dict[str, Any] = Field(default_factory=dict)


class ModerationCategory(BaseModel):
    """Single moderation category."""
    model_config = _FROZEN_SLOT


    flagged: bool | None = None
    scores: dict[str, float] = Field(default_factory=dict)


class ModerationResponse(BaseModel):
    """Moderation API response."""
    model_config = _FROZEN_SLOT


    id: str | None = None
    flagged: bool | None = None
    categories: dict[str, bool] = Field(default_factory=dict)


class FileInfo(BaseModel):
    """File info."""
    model_config = _FROZEN_SLOT


    id: str | None = None
    object: str | None = None
    filename: str | None = None
    purpose: str | None = None
    created_at: int | None = None
    size: int | None = None


class FileList(BaseModel):
    """List of files."""
    model_config = _FROZEN_SLOT


    object: str | None = None
    data: list[FileInfo] = Field(default_factory=list)


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]