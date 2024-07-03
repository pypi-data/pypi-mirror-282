# JSONToolkit
 
## JSON Toolkit

**JSONToolkit** is a simple Python library for manipulating JSON files. It allows you to convert JSON files between one-line and multi-line formats easily, as well as add various types of key-value pairs to your JSON data.

## Features

### JSON Conversion
- Convert a JSON file to a single-line JSON string.
```python
# Convert JSON to one-line format
JSONToolkit.convert(json_file_path, 'to-oneline') 
```
- Convert a single-line JSON string back to a multi-line JSON format.
```python
# Convert JSON back to multi-line format
JSONToolkit.convert(json_file_path, 'from-oneline')
```

### Adding Key JSON Elements

- Add a key-value pair to the JSON data.
```python
# Add a key-value pair
JSONToolkit.add_key_value(json_file_path, 'key', value)
```

- Add a JSON object (dictionary).
```python
# Add a JSON object
JSONToolkit.add_object(json_file_path, 'key', {"nested_key": "nested_value"})
```

- Add a string value.
```python
# Add a string value
JSONToolkit.add_string(json_file_path, 'key', 'string_value')
```

- Add a number (integer or float).
```python
# Add a number
JSONToolkit.add_number(json_file_path, 'key', 123)
# or
JSONToolkit.add_number(json_file_path, 'key', 123.45)
```

- Add a JSON array (list).
```python
# Add a JSON array
JSONToolkit.add_array(json_file_path, 'key', [1, 2, 3])
```

- Add a null value.
```python
# Add a null value
JSONToolkit.add_null(json_file_path, 'key')
```

- Add a boolean value.
```python
# Add a boolean value
JSONToolkit.add_bool(json_file_path, 'key', True)
# or
JSONToolkit.add_bool(json_file_path, 'key', False)
```

## Installation

You can install the library using pip:

```sh
pip install json-toolkit
