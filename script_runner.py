from commands import *

class ScriptRunner:
    def __init__(flavored, data):
        self.script = flavored.script
        self.commands = flavored.commands
        self.data = data

    def run():
        for command in self.script:
            if hasattr(self, command):
                getattr(self, command)(self.data)
            else:
                raise RuntimeError("unsupported script command '{0}' detected".format(command))

    def _getArgs(self, data_entity, params):
        args = []
        for param in params:
            if hasattr(data_entity, param):
                args.append(getattr(data_entity, param))
        return args

    def create_groups(data):
        create_group_command = self.commands.create_group.command_line
        for group in data.groups:
            args = _getArgs(group, self.commands.create_group.params)
            result = Command(create_group_command,*args)
        