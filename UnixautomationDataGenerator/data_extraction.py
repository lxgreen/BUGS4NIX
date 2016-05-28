class DataExtractor:
    def extract_data(self, data_sheet):
        pass

class GroupDataExtractor(DataExtractor):
    def extract_data(self, data_sheet):
        result = []
        for i in range(1, data_sheet.max_row):
            if data_sheet.columns[0][i].value == None:
                return result
            result.append({ 'name': data_sheet.columns[0][i].value })
        return result

class UserDataExtractor(DataExtractor):
    _NAME = 0
    _PASSWORD = 1
    _GROUPS = 2
    _SSH_PATH = 3
    _SSH_PHRASE = 4
    _LOCKED = 5

    def extract_data(self, data_sheet):
        result = []
        for i in range(1, data_sheet.max_row):
            if data_sheet.columns[UserDataExtractor._NAME][i].value == None:
                return result
            result.append({
                            'name': data_sheet.columns[UserDataExtractor._NAME][i].value,
                            'password': data_sheet.columns[UserDataExtractor._PASSWORD][i].value,
                            'groups': data_sheet.columns[UserDataExtractor._GROUPS][i].value,
                            'ssh':  {
                                        'path': data_sheet.columns[UserDataExtractor._SSH_PATH][i].value,
                                        'phrase': data_sheet.columns[UserDataExtractor._SSH_PHRASE][i].value                                        
                                    },
                            'locked': data_sheet.columns[UserDataExtractor._LOCKED][i].value 
                          })
        return result

class FileDataExtractor(DataExtractor):
    _OWNER = 0
    _CONTENT = 1
    _MODE = 3
    _NAME = 4

    def extract_data(self, data_sheet):
        result = []
        for i in range(1, data_sheet.max_row):
            if data_sheet.columns[FileDataExtractor._NAME][i].value == None:
                return result
            result.append({
                            'name': data_sheet.columns[FileDataExtractor._NAME][i].value,
                            'mode': data_sheet.columns[FileDataExtractor._MODE][i].value,
                            'content': data_sheet.columns[FileDataExtractor._CONTENT][i].value,                            
                            'owner': data_sheet.columns[FileDataExtractor._OWNER][i].value
                          })
        return result

class DirectoryDataExtractor(DataExtractor):
    _OWNER = 0    
    _MODE = 2
    _NAME = 3

    def extract_data(self, data_sheet):
        result = []
        for i in range(1, data_sheet.max_row):
            if data_sheet.columns[DirectoryDataExtractor._NAME][i].value == None:
                return result
            result.append({
                            'name': data_sheet.columns[DirectoryDataExtractor._NAME][i].value,
                            'mode': data_sheet.columns[DirectoryDataExtractor._MODE][i].value,                              
                            'owner': data_sheet.columns[DirectoryDataExtractor._OWNER][i].value
                          })
        return result


class DataExtractorFactory:
    _extractors = {
                    'Groups': GroupDataExtractor(),
                    'Users': UserDataExtractor(),
                    'Files': FileDataExtractor(),
                    'Directories': DirectoryDataExtractor()
                  }    
    
    def get_extractor(self, sheet_name):
        return DataExtractorFactory._extractors[sheet_name]