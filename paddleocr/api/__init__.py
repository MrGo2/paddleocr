# Copyright (c) 2025 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""PaddleOCR API Module.

This module provides type definitions, protocols, and utilities for working
with PaddleOCR in a type-safe manner. It is designed to improve developer
experience through better IDE support and type checking.

Basic Usage:
    Import types for type hints::

        from paddleocr.api import ImageInput, OCRResult, TextLine

    Use protocols for generic functions::

        from paddleocr.api import Pipeline

        def run_pipeline(pipeline: Pipeline, images: list[str]) -> list:
            results = []
            for image in images:
                results.extend(pipeline.predict(image))
            return results

    Use configuration types::

        from paddleocr.api import OCRConfig, DeviceConfig

        config: OCRConfig = {
            "lang": "en",
            "ocr_version": "PP-OCRv5",
            "device": {"device": "gpu:0", "precision": "fp16"},
        }

Type Definitions:
    - :data:`ImageInput`: Union type for image inputs (path, URL, or array)
    - :data:`BoundingBox`: Four corner points of a text region
    - :data:`Point`: A single (x, y) coordinate
    - :data:`PrecisionType`: Literal type for precision settings

Configuration Types:
    - :class:`DeviceConfig`: Device and inference settings
    - :class:`TextDetectionConfig`: Text detection model settings
    - :class:`TextRecognitionConfig`: Text recognition model settings
    - :class:`OCRConfig`: Complete OCR pipeline configuration

Result Types:
    - :class:`TextLine`: Single detected text line with confidence
    - :class:`TableCell`: Single cell in a detected table
    - :class:`TableResult`: Complete table detection result
    - :class:`LayoutElement`: Detected layout element (text, table, figure)
    - :class:`FormulaResult`: Detected mathematical formula

Protocol Classes:
    - :class:`Predictor`: Interface for single-model predictors
    - :class:`Pipeline`: Interface for multi-model pipelines
    - :class:`OCRResult`: Interface for OCR result objects
"""

from __future__ import annotations

from .types import (
    # Basic types
    BoundingBox,
    DeviceType,
    ImageInput,
    OCRVersion,
    Point,
    PrecisionType,
    ProgressCallback,
    RectBox,
    ResultCallback,
    # Configuration types
    DeviceConfig,
    OCRConfig,
    TextDetectionConfig,
    TextRecognitionConfig,
    # Result types
    FormulaResult,
    LayoutElement,
    OCRResult,
    TableCell,
    TableResult,
    TextLine,
    TextLineWithWordBoxes,
    # Protocol classes
    Pipeline,
    Predictor,
)

__all__ = [
    # Basic types
    "ImageInput",
    "Point",
    "BoundingBox",
    "RectBox",
    "PrecisionType",
    "OCRVersion",
    "DeviceType",
    # Configuration types
    "DeviceConfig",
    "TextDetectionConfig",
    "TextRecognitionConfig",
    "OCRConfig",
    # Result types
    "TextLine",
    "TextLineWithWordBoxes",
    "TableCell",
    "TableResult",
    "LayoutElement",
    "FormulaResult",
    # Protocol classes
    "Predictor",
    "Pipeline",
    "OCRResult",
    # Callback types
    "ProgressCallback",
    "ResultCallback",
]
