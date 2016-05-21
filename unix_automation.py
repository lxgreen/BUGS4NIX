import argparse

from json_file_parser import JSONFileParser, FileParserError
from os_detector import OSDetector
from script_runner import ScriptRunner


def main():
    # Get the data and commands file paths from command line
    cli_parser = argparse.ArgumentParser(description='Unix Automation Console')
    cli_parser.add_argument('--data', dest='data_path', type=str, default='./data.json', 
                        help='path to data.json containing desired users, groups, files, and ssh keys ' 
                        'configuration info (default: ./data.json)')
    cli_parser.add_argument('--commands', dest='commands_path', type=str, default='./commands.json', 
                        help='path to commands.json containing the supported OS flavors info (default: ./commands.json)')
    args = cli_parser.parse_args()
    try:
        file_parser = JSONFileParser(args.commands_path, args.data_path)
        os_detector = OSDetector(file_parser.commands['agnostic'])
        flavor_id = os_detector.detect_flavor()
        script_runner = ScriptRunner(file_parser.commands[flavor_id], file_parser.data)
        script_runner.run();          
    except Exception as error:
        print 'Error: {0}'.format(error.message)
    return 0

if __name__ == "__main__":
    main()
