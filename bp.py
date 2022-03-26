try:
    import gdb
except ImportError as e:
    raise ImportError("This script must be run in GDB: ", str(e))

class BreakPoint(gdb.Breakpoint):
    '''create a breakpoint at `bp_expr`, call the cb when the breakpoint hit, stop if stop=true'''
    def __init__(self, bp_expr, callback, stop=False, temporary=False):
        gdb.Breakpoint.__init__(self, bp_expr, gdb.BP_BREAKPOINT, False, temporary)
        self.silent = True
        self._callback = callback
        self._stop = stop

    def stop(self):
        stop_after_callback = self._callback()
        return self._stop and stop_after_callback


class FinishBreakpoint(gdb.FinishBreakpoint):
    def __init__(self, cb) -> None:
        super().__init__()
        self._callback = cb
    def stop(self):
        print("normal finish")
        try:
            if self._callback:
                self._callback()
        except RuntimeError as e:
            print(e)
        return False

    def out_of_scope():
        print("abnormal finish, do not run the call back")

class WatchPoint(gdb.Breakpoint):
    '''
       gdb watchpoint expression '..'
           doesn't work. It will complains 'You may have requested too many hardware breakpoints/watchpoints.'
           The workaround is set wp by address, like 'watch *(long *) 0xa0f74d8'
       '''

    def __init__(self, expr, cb):
        self.expr = expr
        self.val = gdb.parse_and_eval(self.expr)
        self.address = self.val.address
        self.ty = gdb.lookup_type('int')
        addr_expr = '*(int*)' + str(self.address)
        gdb.Breakpoint.__init__(self, addr_expr, gdb.BP_WATCHPOINT)
        self.silent = True
        self.callback = cb

    def stop(self):
        addr = int(str(self.address), 16)
        val_buf = gdb.selected_inferior().read_memory(addr, 4)
        val = gdb.Value(val_buf, self.ty)
        print('symbal value = ' + str(val))
        self.callback()
        return False
