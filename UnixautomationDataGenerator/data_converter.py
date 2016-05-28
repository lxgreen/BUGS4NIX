import argparse

from excel_helper import ExcelHelper
from json_data_writer import JSONDataWriter


def main():
    # Get the data file paths from command line
    cli_parser = argparse.ArgumentParser(description='Unix Automation Data Generation Utility')
    cli_parser.add_argument('--in', dest='data_input', type=str, default='./data.xlsx', 
                            help='path to Excel file containing desired users, groups, files, and dirs ' 
                            'configuration info (default: ./data.xlsx)')
    cli_parser.add_argument('--out', dest='data_output', type=str, default='./data.json', 
                            help='path to data.json containing the desired users, groups, files, and dirs ' 
                            'configuration info (default: ./data.json)')
    args = cli_parser.parse_args()
    try:
        data_writer = JSONDataWriter(args.data_output)
        excel_reader = ExcelHelper(args.data_input)
        for sheet in excel_reader.get_sheet_names():
            data = excel_reader.extract_sheet_data(sheet)
            data_writer.process_data(data, sheet)
        data_writer.write_data()
    except Exception as error:
        print 'Error: {0}'.format(error.message)
    return 0

if __name__ == "__main__":
    main()

