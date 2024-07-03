import json


class JSONToolkit:
    @staticmethod
    def convert(file_path: str, operation: str):
        with open(file_path, 'r') as file:
            data = json.load(file)

        if operation == 'to-oneline':
            json_data = json.dumps(data)
            with open(file_path, 'w') as file:
                file.write(json_data)
        elif operation == 'from-oneline':
            json_data = json.dumps(data, indent=4)
            with open(file_path, 'w') as file:
                file.write(json_data)
        else:
            raise ValueError("Operation must be either 'to-oneline' or 'from-oneline'.")

    @staticmethod
    def add_key_value(file_path: str, key: str, value):
        with open(file_path, 'r') as file:
            data = json.load(file)

        data[key] = value

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def add_object(file_path: str, key: str, obj: dict):
        JSONToolkit.add_key_value(file_path, key, obj)

    @staticmethod
    def add_string(file_path: str, key: str, string: str):
        JSONToolkit.add_key_value(file_path, key, string)

    @staticmethod
    def add_number(file_path: str, key: str, number: (int, float)):
        JSONToolkit.add_key_value(file_path, key, number)

    @staticmethod
    def add_array(file_path: str, key: str, array: list):
        JSONToolkit.add_key_value(file_path, key, array)

    @staticmethod
    def add_null(file_path: str, key: str):
        JSONToolkit.add_key_value(file_path, key, None)

    @staticmethod
    def add_bool(file_path: str, key: str, bool_value: bool):
        JSONToolkit.add_key_value(file_path, key, bool_value)

    @staticmethod
    def remove_key(file_path: str, key: str):
        with open(file_path, 'r') as file:
            data = json.load(file)

        if key in data:
            del data[key]
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        else:
            raise ValueError(f"Key '{key}' was not found in the JSON file.")
