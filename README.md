# BUGS for *NIX
## DESCRIPTION
BUGS is an acronym for "Batch Users, Groups, Sudo/SSH". It allows automatic user/group creation and configuration for *NIX systems.

## FEATURES
* Groups:
	* Creation
	* Sudoers configuration
* Users:
	* Creation
	* Sudoers configuration
	* Joining a group
	* SSH configuration
	* Account lock-down
* Files and directories:
	* Creation
	* Access mode configuration
	* Owner configuration

## PREREQUISITES
* Python 2.7
* Excel supporting software (for data generation)

## USAGE
The BUGS consists of two components: Data Converter and Unix Automation. The former allows to generate the desired data via Excel tool. The latter is supposed to be deployed to a tagret machine to automate the desired operations.

### Data Converter
The Data Converter component contains the predefined Excel document `data.xlsx`. This document contains 4 sheets: Groups, Users, Files and Directories. Each sheet has some sample data. The user is intended to input the desired data to the document, and then run the `data_converter.py` script. 
By default, the script is looking for `data.xlsx` in the same directory, and writes its output to `data.json` at the upper level.
These defaults can be overridden by providing `--in` and `--out` parameters to the script.
The Data Converter can be run locally, and only its output file (`data.json`) should be deployed to a target machine.

### Unix Automation
The Unix Automation component consists of Python modules and two JSON files: `data.json` and `commands.json`. 
The `data.json` file is discussed in previous section. The `commands.json` contains the specific command syntax according to the *NIX flavor. 
This file should be edited only when there is a new flavor needs to be supported. Currently, there are two Linux flavors supported (CentOS and Fedora).
Before the automation tasks could be performed, the Unix Automation directory has to be deployed to the target system, including both JSON files.
The main script `unix_automation.py` should run as `root`.
By default, the script looks for the both JSON files in the same directory. This can be overridden by providing the `--data` and `--commands` parameters to the script.
At the moment, every command execution is logged to the console.