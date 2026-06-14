# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for OpenAI API responses."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class ModelInfo(BaseModel, frozen=True, slots=True):
    """OpenAI model info."""

    id: str
    object: str | None = None
    created: int | None = None
    owned_by: str | None = None


class ModelList(BaseModel, frozen=True, slots=True):
    """List of models."""

    object: str | None = None
    data: list[ModelInfo] = Field(default_factory=list)


class EmbeddingItem(BaseModel, frozen=True, slots=True):
    """Single embedding result."""

    embedding: list[float]
    index: int | None = None
    object: str | None = None


class EmbeddingResponse(BaseModel, frozen=True, slots=True):
    """Embedding API response."""

    object: str | None = None
    model: str | None = None
    embeddings: list[list[float]] = Field(default_factory=list)
    usage: dict[str, Any] = Field(default_factory=dict)


class ModerationCategory(BaseModel, frozen=True, slots=True):
    """Single moderation category."""

    flagged: bool | None = None
    scores: dict[str, float] = Field(default_factory=dict)


class ModerationResponse(BaseModel, frozen=True, slots=True):
    """Moderation API response."""

    id: str | None = None
    flagged: bool | None = None
    categories: dict[str, bool] = Field(default_factory=dict)


class FileInfo(BaseModel, frozen=True, slots=True):
    """File info."""

    id: str | None = None
    object: str | None = None
    filename: str | None = None
    purpose: str | None = None
    created_at: int | None = None
    size: int | None = None


class FileList(BaseModel, frozen=True, slots=True):
    """List of files."""

    object: str | None = None
    data: list[FileInfo] = Field(default_factory=list)


# Type aliases
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]