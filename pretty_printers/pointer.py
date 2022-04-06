# # printer is to pretty print the variable
# # 1 create a printer with to_string method
# # 2 create a printer matcher
# # 3 register the printer to the gdb.

import re
import gdb.printing
import gdb
import traceback
import common
gPrinters = {}

def lookup_pretty_printer(val):
    try:
        tp = val.type
        if val.type.code == gdb.TYPE_CODE_PTR:
            tp = common.norm_type(val.type)
            if int(val) == 0:
                return None
        for k, v in gPrinters.items():
            if k.search(str(tp)):
                return v(val)
    except Exception as e:
        print(traceback.format_exc())
    return None


print('register disptacher for pointer.')
gdb.printing.register_pretty_printer(
    gdb.current_objfile(),
    lookup_pretty_printer, replace=True
)
