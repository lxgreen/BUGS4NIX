import json

from data_processing import *


class JSONDataWriter:
    _processor_factory = DataProcessorFactory()

    def __init__(self, json_file):
        self._json_file = json_file
        self._data = {}

    def process_data(self, data, sheet_name):
        data_processor = JSONDataWriter._processor_factory.get_processor(sheet_name)
        data_processor.process_data(data, self._data)
        print '{0} data processed'.format(sheet_name)

    def write_data(self):
        with open(self._json_file, 'w') as data_file:
            json.dump(self._data, data_file)