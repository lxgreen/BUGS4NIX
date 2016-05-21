import subprocess


class CommandResult:
    SUCCESS_CODE = 0    

    def __init__(self, output, return_code, command):        
        self.output = output
        self.return_code = return_code
        self.command = command

class Command:
    def __init__(self, command, params):
        self._command = command
        self._params = params    

    def execute(self):
        command_line = self._command
        if self._params is not None:
            command_line = command_line.format(*self._params)
        try:  
            output = subprocess.check_output(command_line, shell=True)    
            return_code = CommandResult.SUCCESS_CODE
            print "command '{0}' executed successfully".format(command_line)
        except subprocess.CalledProcessError as error:
            output = error.output
            return_code = error.returncode            
        return CommandResult(output, return_code, command_line)
