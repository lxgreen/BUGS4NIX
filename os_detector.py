from commands import *

class OSDetector:  
    def __init__(self, commands):
        self._commands = commands['commands']
        self._flavors = commands['supported_flavors']

    def _is_os(self, os_id):
        releaseTest = Command(self._commands['test_etc_release']['command_line'], {os_id})
        versionTest = Command(self._commands['test_proc_version']['command_line'], {os_id})
        lsbReleaseTest = Command(self._commands['test_lsb_release']['command_line'], {os_id})
        result = releaseTest.execute()
        if result.output:
            return True
        result = versionTest.execute()
        if result.output:
            return True
        result = lsbReleaseTest.execute()
        return bool(result.output)

    def detect_flavor(self):
        for flavor in self._flavors:
            if self._is_os(flavor):
                return flavor
        raise NotImplementedError("The current OS is not supported yet")

    