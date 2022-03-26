try:
    import gdb
except ImportError as e:
    raise ImportError("This script must be run in GDB: ", str(e))


def print_stack_trace():
    gdb.execute('bt')
