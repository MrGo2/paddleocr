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

"""Deprecation utilities for PaddleOCR.

This module provides utilities for handling deprecated parameters and CLI options.
"""

from __future__ import annotations

import argparse
import warnings
from typing import Any, Optional, Sequence, Union

from typing_extensions import deprecated as deprecated


class CLIDeprecationWarning(DeprecationWarning):
    """Warning class for deprecated CLI options."""

    pass


class DeprecatedOptionAction(argparse.Action):
    """Argparse action that warns when a deprecated option is used."""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Union[str, Sequence[Any], None],
        option_string: Optional[str] = None,
    ) -> None:
        """Handle the deprecated option usage.

        Args:
            parser: The ArgumentParser object.
            namespace: The Namespace object that will be returned by parse_args().
            values: The associated command-line arguments.
            option_string: The option string that was used to invoke this action.
        """
        if option_string is None:
            raise ValueError("option_string cannot be None for deprecated options")
        warnings.warn(
            f"The option `{option_string}` has been deprecated and will be removed "
            "in the future. Please refer to the documentation for more details.",
            CLIDeprecationWarning,
        )
        setattr(namespace, self.dest, values)


def warn_deprecated_param(name: str, new_name: Optional[str] = None) -> None:
    """Emit a deprecation warning for a parameter.

    Args:
        name: The name of the deprecated parameter.
        new_name: The name of the new parameter to use instead, if applicable.
    """
    msg = (
        f"The parameter `{name}` has been deprecated and will be removed in the future."
    )
    if new_name is not None:
        msg += f" Please use `{new_name}` instead."
    warnings.warn(msg, DeprecationWarning, stacklevel=3)
