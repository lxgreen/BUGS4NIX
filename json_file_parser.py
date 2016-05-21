import os.path as path
import json

class FileParserError(Exception):
    def __init__(self, message):
        self.message = message

class JSONFileParser:
    def __init__(self, commands_file_path, data_file_path):
        if not path.isfile(commands_file_path) or not path.isfile(data_file_path):
            raise FileParserError("invalid configuration: bad file path/s")

        commands_file = None
        data_file = None
        try:  
            with open(commands_file_path) as commands_file:               
                self.commands = json.load(commands_file)

            with open(data_file_path) as data_file:
                self.data = json.load(data_file)
            # TODO: validate commands and data object structure
        except Exception as error:
            raise FileParserError(error.message)
