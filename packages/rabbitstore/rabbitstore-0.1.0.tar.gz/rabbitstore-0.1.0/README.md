# RabbitStore

RabbitStore is a Python module for storing and retrieving key-value pairs using RabbitMQ. It ensures that only the latest value is stored and can be retrieved multiple times.

## Installation

Install the package using pip:

```bash
pip install rabbitstore
```

## Usage
```python
from rabbitstore import RabbitStore

# Set value
RabbitStore.set('my_key', {'data': 'value'}, host='localhost', username='guest', password='guest')

# Get value
value = RabbitStore.get('my_key', host='localhost', username='guest', password='guest')
print(value)

# Remove value
RabbitStore.set('my_key', None, host='localhost', username='guest', password='guest')
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
