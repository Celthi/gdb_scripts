
try:
    import gdb
except ImportError as e:
    raise ImportError("This script must be run in GDB: ", str(e))

gProcess = None
class Process:
    def __init__(self):
        self._inferior = gdb.selected_inferior()
        self.types = {}

    def read_memory(self, addr, size):
        return self._inferior.read_memory(addr, size)

    def lookup_type(self, tp):
        if tp in self.types:
            return self.types[tp]
        _tp = gdb.lookup_type(tp)
        self.types[tp] = _tp
        return _tp

def get_process():
    global gProcess
    if not gProcess:
        gProcess = Process()
    return gProcess
