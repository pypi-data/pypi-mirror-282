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
