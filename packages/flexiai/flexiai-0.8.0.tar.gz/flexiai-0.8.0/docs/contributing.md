
# Contributing to FlexiAI

We welcome contributions to the FlexiAI framework! Please read the following guidelines to get started.

## How to Contribute

1. **Fork the repository**: Click the 'Fork' button on the top right corner of the repository page to create a copy of the repository in your own GitHub account.

2. **Clone your fork**: Clone your forked repository to your local machine.

    ```bash
    git clone https://github.com/SavinRazvan/flexiai.git
    cd flexiai
    ```

3. **Create a branch**: Create a new branch for your feature or bugfix.

    ```bash
    git checkout -b my-feature-branch
    ```

4. **Make changes**: Make your changes to the codebase. Ensure that your code follows the project's coding standards.

5. **Add tests**: If you added new functionality, make sure to add tests for it in the `tests/` directory.

6. **Commit your changes**: Commit your changes with a clear and concise commit message.

    ```bash
    git add .
    git commit -m "Add new feature"
    ```

7. **Push to your fork**: Push your changes to your forked repository.

    ```bash
    git push origin my-feature-branch
    ```

8. **Open a pull request**: Go to the original repository and open a pull request. Provide a clear description of your changes and any related issues.

## Code of Conduct

Please adhere to the [Code of Conduct](link-to-code-of-conduct) when contributing to this project.

## Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Write clear and concise commit messages.
- Ensure your code is well-documented with comments and docstrings.

## Reporting Issues

If you encounter any issues, please open an issue on GitHub with detailed information about the problem.

## Pull Request Process

1. Ensure your code is well-documented.
2. Ensure that your code follows the project's coding standards.
3. Ensure that all tests pass.
4. Describe your pull request in detail, including what problem it solves and why this solution is necessary.

## Testing

To ensure the quality and reliability of the FlexiAI framework, we require that all contributions include tests where applicable.

### Running Tests

You can run the tests using the following commands:

```bash
# Activate your virtual environment
source venv/bin/activate  # For Linux/WSL
venv\Scripts\activate  # For Windows

# Install the test dependencies
pip install -r requirements.txt

# Run the tests
pytest tests/
```

### Writing Tests

Please write tests for any new functionality you add. Place your tests in the `tests/` directory.

Ensure your tests cover the following:

- Unit tests for individual functions and methods
- Integration tests for larger components or workflows

We use [pytest](https://pytest.org/) as our testing framework. Here's a basic example of a test:

```python
import pytest
from core.flexiai_client import FlexiAI

def test_create_thread():
    flexiai = FlexiAI()
    thread = flexiai.create_thread()
    assert thread is not None
    assert hasattr(thread, 'id')
```

## Community

Join our community to stay updated on the latest developments, share your ideas, and collaborate with other contributors.

- [Join the discussion on GitHub Issues](https://github.com/SavinRazvan/flexiai/issues)

Thank you for contributing to FlexiAI!
