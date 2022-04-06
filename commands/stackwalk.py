
# Usage: to load this to gdb run:
# (gdb) source ..../path/to/debug_naughty.py
#
# To have this automatically load, you need to put the script
# in a path related to your binary. If you make /usr/sbin/foo,
# You can ship this script as:
# /usr/share/gdb/auto-load/ <PATH TO BINARY>
# /usr/share/gdb/auto-load/usr/sbin/foo
#
# This will trigger gdb to autoload the script when you start
# to acces a core or the live binary from this location.
#

import gdb


class StackWalkWCharCommand(gdb.Command):
    def __init__(self):
        # This registers our class as "simple_command"
        super(StackWalkWCharCommand, self).__init__("stackwalk", gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        # When we call "simple_command" from gdb, this is the method
        # that will be called.
        print("Hello from simple_command!")
        # get the register
        rbp = gdb.parse_and_eval('$rbp')
        rsp = gdb.parse_and_eval('$rsp')
        ptr = rsp
        ppwc = gdb.lookup_type('wchar_t').pointer().pointer()
        while ptr < rbp:
            try:
                print('pointer is {}'.format(ptr))
                print(gdb.execute('wc_print {}'.format(
                    ptr.cast(ppwc).dereference())))
                print('===')
            except:
                pass
            ptr += 4


# This registers our class to the gdb runtime at "source" time.
StackWalkWCharCommand()
