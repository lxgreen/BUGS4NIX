class CommandResult:
    def __init__(result_text):        
        self.text = result_text
        self.status = "Valid"

class CommandNotFoundResult(CommandResult):
    def __init__():
        self.status = "CommandNotFound"

class EmptyCommandResult(CommandResult):
    def __init__():
        self.status = "Empty"

class CommandResultFactory:
    # TODO: flavor-dependent?
    @staticmethod
    def _command_not_found(result):
        return ('command not found' in result)

    @staticmethod
    def get_result(result_text):
        if result_text == "":
            return EmptyCommandResult()
        elif CommandResultFactory._command_not_found(result_text):
            return CommandNotFoundResult()   
        else:
            return CommandResult(result_text)

class Command:
    def __init__(command, params):
        self._command = command
        self._params = params    

    def execute(self):
        command_line = self._command
        if self._params is not None:
            command_line = command_line.format(*self._params)

        result = subprocess.check_output(command_line, shell=True)       

        return CommandResultFactory.get_result(result)
