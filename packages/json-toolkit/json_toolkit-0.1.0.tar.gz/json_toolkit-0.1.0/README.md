# JSONToolkit
 
## JSON Toolkit

JSON Manipulator is a simple Python library for manipulating JSON files. It allows you to convert JSON files between one-line and multi-line formats easily.

## Features

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
## Installation

You can install the library using pip:

```sh
pip install json-toolkit
