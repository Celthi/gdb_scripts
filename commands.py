try:
    import gdb
except ImportError as e:
    raise ImportError("This script must be run in GDB: ", str(e))


class SampleCommand(gdb.Command):
    '''
       Your custom gdb command
       '''
    _command = "sample_command"

    def __init__(self):
        gdb.Command.__init__(self, self._command, gdb.COMMAND_STACK)

    def invoke(self, argument, from_tty):
        print('command is called.')
