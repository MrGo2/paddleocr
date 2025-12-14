# Changelog

All notable changes to PaddleOCR will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.3.0] - 2025-10-16

### Added

- **PaddleOCR-VL**: A SOTA and resource-efficient vision-language model for document parsing
  - Supports 109 languages
  - Excels in recognizing complex elements (text, tables, formulas, charts)
  - Available on [HuggingFace](https://huggingface.co/PaddlePaddle/PaddleOCR-VL)
- **PP-OCRv5 Multilingual Recognition Model**: Improved accuracy and coverage for Latin script recognition
  - Added support for Cyrillic, Arabic, Devanagari, Telugu, Tamil, and other language systems
  - Model has only 2M parameters with accuracy improvements over 40% for some models

## [3.2.0] - 2025-08-21

### Added

- Training, inference, and deployment for PP-OCRv5 recognition models in English, Thai, and Greek
- Full support for PaddlePaddle framework versions 3.1.0 and 3.1.1
- Comprehensive upgrade of PP-OCRv5 C++ local deployment solution (Linux and Windows)
- High-performance inference now supports CUDA 12
- High-stability service-oriented deployment solution (fully open-sourced)
- Fine-grained benchmarking support for all production lines

### Fixed

- Resolved issue with failed log saving during model training
- Fixed compatibility issues with newer versions of albumentations dependency
- Fixed deadlock warnings when using tokenizers package in multi-process scenarios
- Fixed inconsistencies in switch behaviors in PP-StructureV3 configuration files

### Changed

- Separated core and optional dependencies
- Enabled support for NVIDIA RTX 50 series graphics cards on Windows
- PP-OCR series models now support returning single-character coordinates

## [3.1.1] - 2025-08-15

### Added

- Added missing methods in PP-ChatOCRv4 class: `save_vector`, `save_visual_info_list`, `load_vector`, `load_visual_info_list`
- Added missing parameters to PPDocTranslation class: `glossary`, `llm_request_interval`
- Added demo to MCP documentation

### Changed

- Changed MCP server dependency to use `puremagic` instead of `python-magic`

### Fixed

- Fixed errors and omissions in production line document translation

## [3.1.0] - 2025-06-29

### Added

- **PP-OCRv5 Multilingual Text Recognition Model**: Support for 37 languages including French, Spanish, Portuguese, Russian, Korean, etc.
- **PP-DocTranslation Pipeline**: Document translation based on PP-StructureV3 and ERNIE 4.5
- **MCP Server**: Supports OCR and PP-StructureV3 pipelines with multiple working modes

### Changed

- Upgraded PP-Chart2Table model with 9.36 percentage point improvement

## [3.0.3] - 2025-06-26

### Fixed

- Resolved issue where `enable_mkldnn` parameter was not effective

## [3.0.2] - 2025-06-19

### Added

- Service invocation examples for C++, Java, Go, C#, Node.js, and PHP
- Android example for PP-OCRv5
- Default upper limit for MKL-DNN cache size

### Changed

- Default download source changed from BOS to HuggingFace
- Improved layout partition sorting algorithm in PP-StructureV3
- Enhanced model selection logic for automatic latest version selection

### Fixed

- Fixed CLI parameters not taking effect in PP-StructureV3
- Fixed `export_paddlex_config_to_yaml` functionality issues
- Fixed `save_path` behavior discrepancy
- Fixed multithreading errors when using MKL-DNN
- Fixed channel order errors in various preprocessing and visualization steps
- Fixed overflow issue in `overlap_ratio` calculation

## [3.0.1] - 2025-06-05

### Changed

- Updated default model configuration for PP-OCRv5 (mobile to server models)
- Updated text line orientation classifier to PP-LCNet_x1_0_textline_ori (99.42% accuracy)
- Optimized PP-LCNet_x0_25_textline_ori (3.3 percentage point improvement)

## [3.0.0] - 2025-05-20

### Added

- **PP-OCRv5**: High-accuracy text recognition for all scenarios
  - Single-model support for five text types (Simplified Chinese, Traditional Chinese, Pinyin, English, Japanese)
  - Improved handwriting recognition
  - 13-point accuracy gain over PP-OCRv4
- **PP-StructureV3**: General-purpose document parsing
  - High-accuracy multi-scene PDF parsing
  - Seal recognition, chart-to-table conversion, table recognition with nested formulas/images
- **PP-ChatOCRv4**: Intelligent document understanding
  - 15-point accuracy gain in key-information extraction
  - Native support for ERNIE 4.5
  - Integration with PP-DocBee2

### Changed

- Major interface changes from PaddleOCR 2.x (see [upgrade notes](https://paddlepaddle.github.io/PaddleOCR/latest/en/update/upgrade_notes.html))

---

For the complete history of changes, please refer to the [GitHub Releases](https://github.com/PaddlePaddle/PaddleOCR/releases) page.
