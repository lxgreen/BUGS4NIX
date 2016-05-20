from commands import *

class OSDetector:  
    def __init__(commands):
        self.commands = commands

    def _is_os(self, os_id):
        releaseTest = Command(self.commands.test_etc_release.command_line, {os_id})
        versionTest = Command(self.commands.test_proc_version.command_line, {os_id})
        lsbReleaseTest = Command(self.commands.test_lsb_release.command_line, {os_id})
        result = releaseTest.execute()
        if result.text:
            return True
        result = versionTest.execute()
        if result.text:
            return True
        result = lsbReleaseTest.execute()
        return bool(result.text)

    def detect_os(self):
        for flavor in self.commands.supported_flavors:
            if _is_os(flavor):
                return flavor
        raise NotImplementedError("The current OS is not supported yet")

    