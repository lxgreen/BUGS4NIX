class DataProcessor:
    def process_data(self, appended, data):
        pass

class GroupDataProcessor(DataProcessor):
    def process_data(self, appended, data):
        data['groups'] = appended

class UserDataProcessor(DataProcessor):
    def process_data(self, appended, data):
        data['users'] = appended

class FileDataProcessor(DataProcessor):
    def process_data(self, appended, data):
        data['files'] = appended

class DirectoryDataProcessor(DataProcessor):
    def process_data(self, appended, data):
        data['dirs'] = appended

class DataProcessorFactory:
    _processors = {
                    'Groups': GroupDataProcessor(),
                    'Users': UserDataProcessor(),
                    'Files': FileDataProcessor(),
                    'Directories': DirectoryDataProcessor()
                  }    
    
    def get_processor(self, sheet_name):
        return DataProcessorFactory._processors[sheet_name]