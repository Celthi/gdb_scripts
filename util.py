try:
    import gdb
except ImportError as e:
    raise ImportError("This script must be run in GDB: ", str(e))


def print_stack_trace():
    gdb.execute('bt')

def dynamic_type(val):
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
