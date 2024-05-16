# 读写yaml文件
import yaml

class YAMLHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_yaml(self):
        try:
            with open(self.file_path, 'r') as file:
                data = yaml.safe_load(file)
                return data
        except FileNotFoundError:
            return f"Error: File '{self.file_path}' not found."
        except yaml.YAMLError as e:
            return f"Error reading YAML file: {e}"

    def write_yaml(self, data):
        try:
            with open(self.file_path, 'w') as file:
                yaml.dump(data, file)
            return f"YAML data written to '{self.file_path}' successfully."
        except yaml.YAMLError as e:
            return f"Error writing YAML file: {e}"
