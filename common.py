
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


def dynamic_value(val):
    '''val must be pointer or a reference'''
    return val.cast(val.dynamic_type)


def norm_type(tp):
    '''return the pointee type if the type is pointter'''
    if tp.code == gdb.TYPE_CODE_PTR:
        pointee_type = tp.target()
        if pointee_type.code == gdb.TYPE_CODE_PTR:
            return norm_type(pointee_type)
        return pointee_type
    return tp


def is_null(val):
    if val.type.code == gdb.TYPE_CODE_PTR:
        return int(val) == 0
    return False


def deref(pointer):
    '''dereference pointer to get value'''
    val = pointer
    if val.type.code == gdb.TYPE_CODE_PTR:
        if is_null(val):
            raise Exception("nullptr")
        val = dynamic_value(val)
        val = val.referenced_value()
        if val.type.code == gdb.TYPE_CODE_PTR:
            if is_null(val):
                raise Exception("nullptr")
            val = dynamic_value(val)
            val = val.referenced_value()
    return val

