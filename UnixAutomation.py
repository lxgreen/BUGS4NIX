import os


if __name__ == "__main__":
    main()

def main():

    return 0

def execute_command(command, params):
    command_line = command.format(*params)
    return os.system(command_line)

def get_os_flavor():
    result = execute_command("cat {0} | grep {1}", {"/etc/*release", "CentOS"})