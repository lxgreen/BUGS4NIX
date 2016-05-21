from commands import *

class OSDetector:  
    def __init__(self, commands):
        self._commands = commands['commands']
        self._flavors = commands['supported_flavors']

    def _is_os(self, os_id):
        test_etc_release = Command(self._commands['test_etc_release']['command_line'], {os_id})
        test_proc_version = Command(self._commands['test_proc_version']['command_line'], {os_id})
        test_lsb_release = Command(self._commands['test_lsb_release']['command_line'], {os_id})
        result = test_etc_release.execute()
        if result.output:
            return True
        result = test_proc_version.execute()
        if result.output:
            return True
        result = test_lsb_release.execute()
        return bool(result.output)

    def detect_flavor(self):
        for flavor in self._flavors:
            if self._is_os(flavor):
                return flavor
        raise NotImplementedError("the current OS is not supported yet")
