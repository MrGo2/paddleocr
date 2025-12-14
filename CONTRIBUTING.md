# Contributing to PaddleOCR

Thank you for your interest in contributing to PaddleOCR! We welcome contributions from the community to help make PaddleOCR better. This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Contributions](#making-contributions)
- [Pull Request Process](#pull-request-process)
- [Code Style Guidelines](#code-style-guidelines)
- [Documentation Guidelines](#documentation-guidelines)
- [Testing](#testing)
- [Community](#community)

## Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in your interactions with other contributors.

## Getting Started

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix issues in the codebase
- **New features**: Add new functionality to PaddleOCR
- **Documentation**: Improve or translate documentation
- **Tests**: Add or improve test coverage
- **Code optimization**: Improve code quality and performance
- **Multi-language support**: Add new language dictionaries and corpora

### Finding Issues to Work On

- Check the [GitHub Issues](https://github.com/PaddlePaddle/PaddleOCR/issues) for open issues
- Look for issues labeled `good first issue` for beginner-friendly tasks
- Issues labeled `help wanted` are good candidates for community contributions

## Development Setup

### Prerequisites

- Python 3.8 or higher (up to 3.12)
- Git
- PaddlePaddle framework (refer to [Installation Guide](https://www.paddlepaddle.org.cn/en/install/quick))

### Setting Up Your Development Environment

1. **Fork the Repository**

   Click the "Fork" button on the [PaddleOCR GitHub page](https://github.com/PaddlePaddle/PaddleOCR) to create your own copy.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/{your_username}/PaddleOCR.git
   cd PaddleOCR
   ```

3. **Add Upstream Remote**

   ```bash
   git remote add upstream https://github.com/PaddlePaddle/PaddleOCR.git
   ```

4. **Install Dependencies**

   ```bash
   # Install the package in development mode
   pip install -e .

   # Install development dependencies
   pip install -r requirements.txt
   pip install pre-commit pytest
   ```

5. **Set Up Pre-commit Hooks**

   ```bash
   pre-commit install
   ```

### Branch Strategy

- `release/x.x`: Stable release branches (default branch)
- `dygraph`: Development branch for new features

For new contributions, create a branch based on the `dygraph` branch:

```bash
git fetch upstream
git checkout -b your-feature-branch upstream/dygraph
```

## Making Contributions

### Creating a Branch

```bash
git checkout -b feature/your-feature-name
# or for bug fixes
git checkout -b fix/issue-description
```

### Making Changes

1. Make your changes following the [Code Style Guidelines](#code-style-guidelines)
2. Add or update tests as needed
3. Update documentation if your changes affect the public API
4. Run pre-commit hooks:

   ```bash
   pre-commit run --all-files
   ```

### Committing Changes

Write clear, concise commit messages:

```bash
git add .
git commit -m "Brief description of changes"
```

**Commit Message Guidelines:**

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep the first line under 72 characters
- Reference issues and pull requests when relevant

## Pull Request Process

### Before Submitting

1. **Sync with upstream**

   ```bash
   git fetch upstream
   git rebase upstream/dygraph
   ```

2. **Run tests**

   ```bash
   pytest tests/
   ```

3. **Run pre-commit checks**

   ```bash
   pre-commit run --all-files
   ```

### Submitting a Pull Request

1. Push your branch to your fork:

   ```bash
   git push origin your-feature-branch
   ```

2. Go to the PaddleOCR repository and click "New Pull Request"

3. Select your branch and fill in the PR template with:
   - A clear title describing the change
   - Description of what the PR does
   - Link to any related issues (use `Fixes #issue_number` to auto-close)
   - Test results or screenshots if applicable

### PR Review Process

- All PRs require review from maintainers
- Address reviewer feedback promptly
- Keep PRs focused - one feature or fix per PR
- Squash commits if you have many small commits

### After Your PR is Merged

- Delete your feature branch
- Update your local repository:

  ```bash
  git checkout dygraph
  git pull upstream dygraph
  ```

## Code Style Guidelines

### Python Code Style

PaddleOCR follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some specific conventions:

- **Formatting**: We use [Black](https://github.com/psf/black) for code formatting
- **Linting**: We use [Flake8](https://flake8.pycqa.org/) for linting
- **Line length**: Maximum 80 characters (enforced by Black)

**Key conventions:**

```python
# Correct spacing
print(x, y)  # After commas

# Correct function defaults
def func(param, default=None):  # No spaces around =
    pass

# Inline comments
x = x + 1  # Two spaces before #, one space after
```

### Docstring Format

Use the Google-style docstring format:

```python
def function_name(param1, param2):
    """Brief description of the function.

    More detailed description if needed.

    Args:
        param1: Description of param1.
        param2: Description of param2.

    Returns:
        Description of return value.

    Raises:
        ValueError: When invalid value is provided.
    """
    pass
```

### Type Hints

We encourage the use of type hints for better code clarity:

```python
from typing import List, Optional, Dict

def process_image(image_path: str, options: Optional[Dict] = None) -> List[str]:
    """Process an image and return recognized text."""
    pass
```

## Documentation Guidelines

### General Guidelines

- Documentation should be provided in both English and Chinese
- Use clear, concise language
- Include code examples where appropriate
- Keep documentation up-to-date with code changes

### File Naming

- Use lowercase with underscores: `add_new_algorithm.md`
- Place images in the `doc/` directory

### Format

- Use proper heading hierarchy (# for title, ## for sections, etc.)
- Code blocks should specify the language:

  ```python
  # Python code example
  ```

- Reference variables and parameters using inline code: `--use_angle_cls`

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_specific.py

# Run with verbose output
pytest -v tests/
```

### Writing Tests

- Place tests in the `tests/` directory
- Follow the naming convention: `test_*.py`
- Use descriptive test names that explain what is being tested
- Include both positive and negative test cases

## Community

### Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion

### Staying Connected

- Star the repository to stay updated
- Follow the [PaddlePaddle WeChat official account](https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/refs/heads/main/images/paddleocr/README/qrcode_for_paddlepaddle_official_account.jpg)

### Recognition

Contributors are recognized in:
- The [Contributors page](https://github.com/PaddlePaddle/PaddleOCR/graphs/contributors)
- Release notes for significant contributions
- Community contribution documentation

---

Thank you for contributing to PaddleOCR! Your contributions help make OCR technology more accessible to everyone.
