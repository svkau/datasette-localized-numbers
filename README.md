# datasette-localized-numbers

[![PyPI](https://img.shields.io/pypi/v/datasette-localized-numbers.svg)](https://pypi.org/project/datasette-localized-numbers/)
[![Changelog](https://img.shields.io/github/v/release/vitlais/datasette-localized-numbers?include_prereleases&label=changelog)](https://github.com/vitlais/datasette-localized-numbers/releases)
[![Tests](https://github.com/vitlais/datasette-localized-numbers/workflows/Test/badge.svg)](https://github.com/vitlais/datasette-localized-numbers/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/vitlais/datasette-localized-numbers/blob/main/LICENSE)

Adds filter for Ninja to show localized numbers.

## Installation

Install this plugin in the same environment as Datasette.
```bash
datasette install datasette-localized-numbers
```
## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd datasette-localized-numbers
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
pytest
```
