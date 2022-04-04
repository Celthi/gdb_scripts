# printer is to pretty print the variable
# 1 create a printer with to_string method
# 2 create a printer matcher
# 3 register the printer to the gdb.
import re
import gdb.printing
import sys


class GUIDPrinter:
    '''
    Currently, only tests in Linux
        typedef struct _GUID
        {
                unsigned int Data1;
                unsigned short Data2;
                unsigned short Data3;
                unsigned char Data4[ 8 ];
        } 
        GUID;
    '''

    def __init__(self, val):

        self.val = val

    def to_string(self):
        guidstr = '{:08X}{:04X}{:04X}{:02X}{:02X}{:02X}{:02X}{:02X}{:02X}{:02X}{:02X}'.format(
            int(self.val['Data1']),
            int(self.val['Data3']),
            int(self.val['Data2']),
            int(self.val['Data4'][3]),
            int(self.val['Data4'][2]),
            int(self.val['Data4'][1]),
            int(self.val['Data4'][0]),
            int(self.val['Data4'][7]),
            int(self.val['Data4'][6]),
            int(self.val['Data4'][5]),
            int(self.val['Data4'][4]))
        return guidstr


def build_pretty_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter("Base")
    print('register DSS ID printer.')
    pp.add_printer('DSS ID printer', '^(DSS_ID|_GUID)', GUIDPrinter)
    return pp


gdb.printing.register_pretty_printer(
    gdb.current_objfile(),
    build_pretty_printer(), replace=True)
