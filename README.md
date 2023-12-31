# datasette-localized-numbers

[![Changelog](https://img.shields.io/github/v/release/svkau/datasette-localized-numbers?include_prereleases&label=changelog)](https://github.com/svkau/datasette-localized-numbers/releases)
[![Tests](https://github.com/svkau/datasette-localized-numbers/workflows/Test/badge.svg)](https://github.com/svkau/datasette-localized-numbers/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/svkau/datasette-localized-numbers/blob/main/LICENSE)

Uses [Babel](https://github.com/python-babel/babel) to add some localisation features to [Datasette](https://github.com/simonw/datasette).

- Render formatted cell-values, e.g. 1234567 > 1 234 567 and 1234567 > 1 234 567,00 kr
- Filters for Ninja2 to show localized numbers.
- Custom SQL functions.

## Installation

Install this plugin in the same environment as Datasette.
```bash
datasette install datasette-localized-numbers
```
## Usage

### Render localized number and currency

### Filter for Ninja2 templates

(sv_SE only!)

```
{{ value|localized_number }}

{{ value|localized_currency }}
```

### Custom SQL function

(sv_SE only!)

```
SELECT(localized_number(1234567))
```

Result: "1 234 567" 

```
SELECT(localized_currency(1234567))
```

Result: "1 234 567,00 kr"

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
