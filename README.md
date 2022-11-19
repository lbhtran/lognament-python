# lognament-python

Lognament is a Python library that provides you with logging decorators.

## Design

- decorators
    - base decorator
    - base function decorator
    - base class decorator
- messages
    - message_manager
    - header
    - info
    - debug
    - warning
    - error
    - footer

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install lognament-python.

```bash
pip install lognament-python
```

## Usage

```python
from lognament import log_function


@log_function
def do_something():
    ...
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
