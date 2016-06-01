class DataExtractor:
    def extract_data(self, data_sheet):
        pass

class GroupDataExtractor(DataExtractor):
    _NAME = 0
    _SUDOERS = 1
    def extract_data(self, data_sheet):
        result = []
        name_column = data_sheet.columns[UserDataExtractor._NAME]        
        sudoers_column = data_sheet.columns[UserDataExtractor._SUDOERS]        
        for i in range(1, data_sheet.max_row):
            if name_column[i].value == None:
                return result
            result.append({ 'name': name_column[i].value,
                            'sudoers': sudoers_column[i].value 
                          })
        return result

class UserDataExtractor(DataExtractor):
    _NAME = 0
    _PASSWORD = 1
    _GROUPS = 2
    _SSH_PATH = 3
    _SSH_PHRASE = 4
    _LOCKED = 5
    _SUDOERS = 6

    def extract_data(self, data_sheet):
        result = []
        name_column = data_sheet.columns[UserDataExtractor._NAME]
        password_column = data_sheet.columns[UserDataExtractor._PASSWORD]
        groups_column = data_sheet.columns[UserDataExtractor._GROUPS]
        path_column = data_sheet.columns[UserDataExtractor._SSH_PATH]
        phrase_column = data_sheet.columns[UserDataExtractor._SSH_PHRASE]
        locked_column = data_sheet.columns[UserDataExtractor._LOCKED]
        sudoers_column = data_sheet.columns[UserDataExtractor._SUDOERS]
        for i in range(1, data_sheet.max_row):
            if name_column[i].value == None:
                return result
            result.append({
                            'name': name_column[i].value,
                            'password': password_column[i].value,
                            'groups': groups_column[i].value,
                            'ssh':  {
                                        'path': path_column[i].value,
                                        'phrase': phrase_column[i].value                                        
                                    },
                            'locked': locked_column[i].value,
                            'sudoers': sudoers_column[i].value
                          })
        return result

class FileDataExtractor(DataExtractor):
    _OWNER = 0
    _CONTENT = 1
    _MODE = 3
    _NAME = 4

    def extract_data(self, data_sheet):
        result = []
        name_column = data_sheet.columns[DirectoryDataExtractor._NAME]
        mode_column = data_sheet.columns[DirectoryDataExtractor._MODE]
        owner_column = data_sheet.columns[DirectoryDataExtractor._OWNER]
        content_column = data_sheet.columns[FileDataExtractor._CONTENT]
        for i in range(1, data_sheet.max_row):
            if name_column[i].value == None:
                return result
            result.append({
                            'name': name_column[i].value,
                            'mode': mode_column[i].value,
                            'content': content_column[i].value,                            
                            'owner': owner_column[i].value
                          })
        return result

class DirectoryDataExtractor(DataExtractor):
    _OWNER = 0    
    _MODE = 2
    _NAME = 3

    def extract_data(self, data_sheet):
        result = []
        name_column = data_sheet.columns[DirectoryDataExtractor._NAME]
        mode_column = data_sheet.columns[DirectoryDataExtractor._MODE]
        owner_column = data_sheet.columns[DirectoryDataExtractor._OWNER]
        for i in range(1, data_sheet.max_row):
            if name_column[i].value == None:
                return result
            result.append({
                            'name': name_column[i].value,
                            'mode': mode_column[i].value,                              
                            'owner': owner_column[i].value
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