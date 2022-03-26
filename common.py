
try:
    import gdb
except ImportError as e:
    raise ImportError("This script must be run in GDB: ", str(e))

def disable_prompt():
    gdb.execute("set pagination off")
    gdb.execute ('set confirm off')

def not_handle_SIGSEGV():
    '''usuall for java, we don't need to handle SIGSEGV'''
    gdb.execute("handle SIGSEGV nostop noprint pass")

def enable_logging(logging_file):
    gdb.execute('set logging file ' + logging_file)
    gdb.execute('set logging on')
