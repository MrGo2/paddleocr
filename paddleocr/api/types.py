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

"""Type definitions for PaddleOCR API.

This module provides type hints and type definitions for the PaddleOCR package,
enabling better IDE support, type checking, and documentation.

Example:
    Using type hints in your code::

        from paddleocr.api import OCRResult, BoundingBox, TextLine

        def process_results(results: list[OCRResult]) -> list[str]:
            texts = []
            for result in results:
                for line in result.get("text_lines", []):
                    texts.append(line["text"])
            return texts
"""

from __future__ import annotations

from typing import (
    Any,
    Callable,
    Iterator,
    List,
    Literal,
    Protocol,
    Tuple,
    TypeVar,
    Union,
    runtime_checkable,
)

from typing_extensions import NotRequired, TypedDict

# =============================================================================
# Basic Types
# =============================================================================

#: Type alias for image input - can be a file path, URL, or numpy array
ImageInput = Union[str, Any]  # str (path/URL) or numpy.ndarray

#: Type alias for a point coordinate (x, y)
Point = Tuple[float, float]

#: Type alias for a bounding box as four corner points
BoundingBox = Tuple[Point, Point, Point, Point]

#: Type alias for a simple rectangular box (x1, y1, x2, y2)
RectBox = Tuple[float, float, float, float]

#: Supported precision types for inference
PrecisionType = Literal["fp32", "fp16"]

#: Supported OCR versions
OCRVersion = Literal["PP-OCRv3", "PP-OCRv4", "PP-OCRv5"]

#: Supported device types
DeviceType = Literal["cpu", "gpu", "npu", "xpu"]


# =============================================================================
# Configuration TypedDicts
# =============================================================================


class DeviceConfig(TypedDict, total=False):
    """Configuration for device settings.

    Attributes:
        device: The device to use for inference (e.g., "cpu", "gpu:0").
        use_tensorrt: Whether to use TensorRT for GPU inference.
        precision: The precision type for inference ("fp32" or "fp16").
        enable_mkldnn: Whether to enable MKL-DNN acceleration on CPU.
        mkldnn_cache_capacity: Cache capacity for MKL-DNN.
        cpu_threads: Number of CPU threads to use.
    """

    device: str
    use_tensorrt: bool
    precision: PrecisionType
    enable_mkldnn: bool
    mkldnn_cache_capacity: int
    cpu_threads: int


class TextDetectionConfig(TypedDict, total=False):
    """Configuration for text detection.

    Attributes:
        model_name: Name of the text detection model.
        model_dir: Directory path to the model.
        limit_side_len: Maximum side length for input image.
        limit_type: Type of limit ("min" or "max").
        thresh: Detection threshold.
        box_thresh: Box threshold for filtering.
        unclip_ratio: Unclip ratio for text region expansion.
        input_shape: Input shape for the model.
    """

    model_name: str
    model_dir: str
    limit_side_len: int
    limit_type: str
    thresh: float
    box_thresh: float
    unclip_ratio: float
    input_shape: Tuple[int, int]


class TextRecognitionConfig(TypedDict, total=False):
    """Configuration for text recognition.

    Attributes:
        model_name: Name of the text recognition model.
        model_dir: Directory path to the model.
        batch_size: Batch size for recognition.
        score_thresh: Score threshold for filtering results.
        input_shape: Input shape for the model.
    """

    model_name: str
    model_dir: str
    batch_size: int
    score_thresh: float
    input_shape: Tuple[int, int]


class OCRConfig(TypedDict, total=False):
    """Complete configuration for OCR pipeline.

    Attributes:
        lang: Language code for OCR.
        ocr_version: Version of OCR to use.
        use_doc_orientation_classify: Whether to classify document orientation.
        use_doc_unwarping: Whether to unwarp documents.
        use_textline_orientation: Whether to classify text line orientation.
        text_detection: Text detection configuration.
        text_recognition: Text recognition configuration.
        device: Device configuration.
    """

    lang: str
    ocr_version: OCRVersion
    use_doc_orientation_classify: bool
    use_doc_unwarping: bool
    use_textline_orientation: bool
    text_detection: TextDetectionConfig
    text_recognition: TextRecognitionConfig
    device: DeviceConfig


# =============================================================================
# Result TypedDicts
# =============================================================================


class TextLine(TypedDict):
    """A single detected text line.

    Attributes:
        text: The recognized text content.
        confidence: Confidence score of the recognition (0-1).
        bounding_box: The four corner points of the text region.
    """

    text: str
    confidence: float
    bounding_box: BoundingBox


class TextLineWithWordBoxes(TextLine):
    """A text line with word-level bounding boxes.

    Attributes:
        word_boxes: List of bounding boxes for each word.
    """

    word_boxes: NotRequired[List[BoundingBox]]


class TableCell(TypedDict):
    """A single table cell.

    Attributes:
        text: The text content of the cell.
        row_start: Starting row index.
        row_end: Ending row index.
        col_start: Starting column index.
        col_end: Ending column index.
        bounding_box: The bounding box of the cell.
    """

    text: str
    row_start: int
    row_end: int
    col_start: int
    col_end: int
    bounding_box: RectBox


class TableResult(TypedDict):
    """Result from table structure recognition.

    Attributes:
        html: HTML representation of the table.
        cells: List of table cells.
        bounding_box: The bounding box of the table.
    """

    html: str
    cells: List[TableCell]
    bounding_box: RectBox


class LayoutElement(TypedDict):
    """A detected layout element.

    Attributes:
        type: The type of layout element (e.g., "text", "table", "figure").
        bounding_box: The bounding box of the element.
        confidence: Confidence score of the detection.
    """

    type: str
    bounding_box: RectBox
    confidence: float


class FormulaResult(TypedDict):
    """Result from formula recognition.

    Attributes:
        latex: LaTeX representation of the formula.
        confidence: Confidence score of the recognition.
        bounding_box: The bounding box of the formula.
    """

    latex: str
    confidence: float
    bounding_box: RectBox


# =============================================================================
# Protocol Classes (Interfaces)
# =============================================================================

# Type variable for result types
ResultT = TypeVar("ResultT")


@runtime_checkable
class Predictor(Protocol[ResultT]):
    """Protocol for predictor classes.

    Predictors are single-model wrappers that perform a specific task
    such as text detection, text recognition, or layout detection.
    """

    def predict(self, input: ImageInput, **kwargs: Any) -> List[ResultT]:
        """Run prediction on input.

        Args:
            input: Image input (path, URL, or numpy array).
            **kwargs: Additional prediction parameters.

        Returns:
            List of prediction results.
        """
        ...

    def predict_iter(self, input: ImageInput, **kwargs: Any) -> Iterator[ResultT]:
        """Run prediction on input, yielding results one at a time.

        Args:
            input: Image input (path, URL, or numpy array).
            **kwargs: Additional prediction parameters.

        Yields:
            Prediction results one at a time.
        """
        ...

    def close(self) -> None:
        """Release resources used by the predictor."""
        ...


@runtime_checkable
class Pipeline(Protocol[ResultT]):
    """Protocol for pipeline classes.

    Pipelines combine multiple models to perform complex tasks
    such as OCR (detection + recognition) or document parsing.
    """

    def predict(self, input: ImageInput, **kwargs: Any) -> List[ResultT]:
        """Run the pipeline on input.

        Args:
            input: Image input (path, URL, or numpy array).
            **kwargs: Additional pipeline parameters.

        Returns:
            List of pipeline results.
        """
        ...

    def predict_iter(self, input: ImageInput, **kwargs: Any) -> Iterator[ResultT]:
        """Run the pipeline on input, yielding results one at a time.

        Args:
            input: Image input (path, URL, or numpy array).
            **kwargs: Additional pipeline parameters.

        Yields:
            Pipeline results one at a time.
        """
        ...

    def close(self) -> None:
        """Release resources used by the pipeline."""
        ...

    def export_paddlex_config_to_yaml(self, yaml_path: str) -> None:
        """Export the pipeline configuration to a YAML file.

        Args:
            yaml_path: Path to save the YAML configuration.
        """
        ...


@runtime_checkable
class OCRResult(Protocol):
    """Protocol for OCR result objects.

    OCR results contain the recognized text and its location in the image.
    """

    def print(self) -> None:
        """Print the result to stdout."""
        ...

    def save_to_img(self, save_path: str) -> None:
        """Save visualization to an image file.

        Args:
            save_path: Directory to save the image.
        """
        ...

    def save_to_json(self, save_path: str) -> None:
        """Save results to a JSON file.

        Args:
            save_path: Directory to save the JSON file.
        """
        ...

    def save_all(self, save_path: str) -> None:
        """Save all outputs (image and JSON).

        Args:
            save_path: Directory to save the outputs.
        """
        ...


# =============================================================================
# Callback Types
# =============================================================================

#: Type for progress callback functions
ProgressCallback = Callable[[int, int], None]

#: Type for result callback functions
ResultCallback = Callable[[Any], None]


# =============================================================================
# Export List
# =============================================================================

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
