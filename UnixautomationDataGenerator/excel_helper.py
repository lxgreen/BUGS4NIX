from openpyxl import load_workbook

from data_extraction import *

class ExcelHelper:
    _extractor_factory = DataExtractorFactory()

    def __init__(self, xslx_file):
        self._work_book = load_workbook(xslx_file, data_only=True, read_only=True)

    def get_sheet_names(self):
        return self._work_book.get_sheet_names()

    def extract_sheet_data(self, sheet_name):
        data_extractor = ExcelHelper._extractor_factory.get_extractor(sheet_name)
        self._work_book[sheet_name].calculate_dimension(force=True)
        return data_extractor.extract_data(self._work_book[sheet_name])

