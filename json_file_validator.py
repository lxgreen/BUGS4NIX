class ValidationResult:
    def __init__(status, reason):
        self._status = status
        self._reason = reason

    def is_valid():
        return self._status == "valid"

    def reason():
        return self._reason

class JSONFileValidator:    
    def __init__(self, commands, data):
        self._commands = commands
        self._data = data

    def validate_commands():
        return validate_commands_root() or validate_agnostic_commands() or validate_supported_flavors() \
                or validate_flavor_structure()

    def validate_commands_root():       
        if not bool(self._commands):
           return ValidationResult("invalid", "commands root object is undefined")
        return None

    def validate_agnostic_commands():
        if not hasattr(self._commands, "agnostic"):
            return ValidationResult("invalid", "agnostic flavor is undefined")
        if not hasattr(self._commands.agnostic, "commands"):
           return ValidationResult("invalid", "agnostic commands are undefined")
        return None

    def validate_supported_flavors():
        if not hasattr(self._commands.agnostic, "supported_flavors"):
            return ValidationResult("invalid", "supported flavors are undefined")
        for flavor in self._commands.agnostic.supported_flavors:
            if not hasattr(self._commands, flavor):
                return ValidationResult("invalid", "the flavor {0} is undefined in commands".format(flavor))
        return None
    
    def validate_flavor_structure():
        for flavor in self._commands.agnostic.supported_flavors:
            if not hasattr(getattr(self._commands, flavor), "commands"):
                return ValidationResult("invalid", "the flavor {0} commands are undefined".format(flavor))
            if not hasattr(getattr(self._commands, flavor), "commands"):
                return ValidationResult("invalid", "the flavor {0} script is undefined".format(flavor))
        return None