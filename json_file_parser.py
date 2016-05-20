import os.path as path
import json

class FileParserError(Exception):
    def __init__(message):
        self.message = message

class JSONFileParser:
    def __init__(commands_file_path, data_file_path):
        if not path.isfile(commands_file_path) or not path.isfile(data_file_path):
            raise FileParserError("invalid configuration: bad file path/s")

        commands_file = None
        data_file = None
        try:  
            commands_file = open(commands_file_path)      
            data_file = open(data_file_path)      
        except IOError as error:
            raise FileParserError(error.message)

        try: 
            self.commands = json.load(commands_file)
            self.data = json.load(data_file)
        except ValueError as error:
            raise FileParserError(error.message)