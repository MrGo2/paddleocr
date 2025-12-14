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

"""CLI utilities for PaddleOCR.

This module provides common utilities for command-line interface operations.
"""

from __future__ import annotations

import argparse
import time
from typing import Any, Dict, List, Optional, Type

from .logging import logger


def str2bool(v: str, /) -> bool:
    """Convert a string to a boolean value.

    Args:
        v: The string to convert.

    Returns:
        True if the string is one of "true", "yes", "t", "y", "1" (case-insensitive),
        False otherwise.
    """
    return v.lower() in ("true", "yes", "t", "y", "1")


def get_subcommand_args(args: argparse.Namespace) -> Dict[str, Any]:
    """Extract subcommand arguments from parsed arguments.

    Removes the 'subcommand' and 'executor' keys from the arguments.

    Args:
        args: The parsed argparse Namespace object.

    Returns:
        A dictionary of arguments with 'subcommand' and 'executor' removed.
    """
    args_dict = vars(args).copy()
    args_dict.pop("subcommand")
    args_dict.pop("executor")
    return args_dict


def add_simple_inference_args(
    subparser: argparse.ArgumentParser, *, input_help: Optional[str] = None
) -> None:
    """Add common inference arguments to a subparser.

    Args:
        subparser: The argument parser to add arguments to.
        input_help: Custom help text for the input argument.
    """
    if input_help is None:
        input_help = "Input path or URL."
    subparser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help=input_help,
    )
    subparser.add_argument(
        "--save_path",
        type=str,
        help="Path to the output directory.",
    )


def perform_simple_inference(
    wrapper_cls: Type[Any],
    params: Dict[str, Any],
    predict_param_names: Optional[List[str]] = None,
) -> None:
    """Perform inference using a wrapper class.

    Args:
        wrapper_cls: The wrapper class to instantiate for inference.
        params: Dictionary of parameters including input, save_path, and model params.
        predict_param_names: List of parameter names to pass to the predict method.
    """
    params = params.copy()

    input_ = params.pop("input")
    save_path = params.pop("save_path")

    if predict_param_names is not None:
        predict_params: Dict[str, Any] = {}
        for name in predict_param_names:
            predict_params[name] = params.pop(name)
    else:
        predict_params = {}
    init_params = params

    wrapper = wrapper_cls(**init_params)

    try:
        result = wrapper.predict_iter(input_, **predict_params)

        t1 = time.time()
        for i, res in enumerate(result):
            logger.info(f"Processed item {i} in {(time.time()-t1) * 1000} ms")
            t1 = time.time()
            res.print()
            if save_path:
                res.save_all(save_path)
    finally:
        wrapper.close()
