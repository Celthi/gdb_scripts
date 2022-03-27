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


import argparse


class DTCommand(gdb.Command):
    def __init__(self):
        # This registers our class as "simple_command"
        super(DTCommand, self).__init__("dt", gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        # When we call "simple_command" from gdb, this is the method
        # that will be called.
        args = arg.split()
        parser = argparse.ArgumentParser(
            description='print the type and offset of fields')
        parser.add_argument('-t', dest='ty', action='store',
                            default='',
                            help='provide the type name')

        args = parser.parse_args(args)
        ty = args.ty
        typ = gdb.lookup_type(ty)
        for field in typ.fields():
            print('+{} {}'.format(field.bitpos/8, field.name))
        


        
DTCommand()
