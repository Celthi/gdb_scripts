try:
    import argparse
    import gdb
except ImportError as e:
    raise ImportError("This script must be run in GDB: ", str(e))

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
        parser.add_argument('tp', 
                            help='provide the type name')

        args = parser.parse_args(args)
        tp = args.tp
        tp = gdb.lookup_type(tp)
        for field in tp.fields():
            print('+{} {}'.format(field.bitpos/8, field.name))


DTCommand()
