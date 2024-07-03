# DynoDino

DynoDino is a set of useful methods to speed up the conversion of objects to AWS services, specifically DynamoDB. This library allows you to easily convert JSON data to DynamoDB format and vice versa.

## Installation

To install the library, use pip:

```bash
pip install dyno-dino
``` 

## Features

### JSON to DynamoDB Conversion

The library provides methods to convert JSON data structures to the format accepted by DynamoDB. This includes converting common data types like strings, numbers, lists, and nested dictionaries.

Example Usage:

```python
from dyno_dino import convert_json_to_dynamodb

json_data = {
    "name": "Victor",
    "phone": "5587975648710",
    "age": 30,
    "is_verified": True,
    "account_balance": 1234.56,
    "nested_object": {
        "key1": "value1",
        "key2": 2
    },
    "list_data": ["item1", "item2", "item3"]
}

dynamodb_data = convert_json_to_dynamodb(json_data)
print(dynamodb_data)
```

### DynamoDB to JSON Conversion

You can also convert data from DynamoDB format back to JSON, making it easier to manipulate and visualize the data.

Example Usage:
```python
from dyno_dino import convert_dynamodb_to_json

dynamodb_data = {
    "M": {
        "name": {"S": "Victor"},
        "phone": {"S": "5587975648710"},
        "age": {"N": "30"},
        "is_verified": {"BOOL": True},
        "account_balance": {"N": "1234.56"},
        "nested_object": {
            "M": {
                "key1": {"S": "value1"},
                "key2": {"N": "2"}
            }
        },
        "list_data": {"L": [
            {"S": "item1"},
            {"S": "item2"},
            {"S": "item3"}
        ]}
    }
}

json_data = convert_dynamodb_to_json(dynamodb_data)
print(json_data)
```

## Available Methods

`convert_json_to_dynamodb(data: dict) -> dict`

> Converts a JSON dictionary to DynamoDB format.
> * Parameters:
>     * `data` (dict): JSON dictionary to be converted.
> * Returns:
>     * Dictionary in DynamoDB format.


`convert_dynamodb_to_json(dynamodb_data: dict) -> dict`

> Converts a DynamoDB format dictionary to JSON.
> * Parameters:
>     * `dynamodb_data` (dict): DynamoDB format dictionary to be converted.
>     * `remove_content` (bool, optional): Whether to remove the "content" key if it exists. Default is `False`
> * Returns:
>     * JSON dictionary.


## Contributing

Contributions are welcome! Feel free to open issues or pull requests on the [GitHub repository](https://github.com/JoaoGodoi/dyno-dino).