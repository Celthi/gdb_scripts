try:
    import gdb
except ImportError as e:
    raise ImportError("This script must be run in GDB: ", str(e))

from libstdcxx.v6.printers import StdMapPrinter, StdVectorPrinter, StdListPrinter
import re


def print_stack_trace():
    gdb.execute('bt')


def StdMapToDict(iMap):
    it = StdMapPrinter('map', iMap).children()
    res = {}
    for key, value in it:
        m = re.search(r'[(\d{1,3})]', key)
        if m:
            count = int(m.group(1))
            if count % 2 == 0:
                # it is key
                k = '{}'.format(value)
            else:          
                res[k] = value.referenced_value()
    return res

def stdVectorToPyList(typename, vector):
    '''
    Given std::vector in gdb.Value, return a list of gdb.Value of the list's elements
    '''
    rslist = []
    elements = StdVectorPrinter(typename, vector).children()
    for (_, val) in iter(elements):
        rslist.append(val)

    return rslist

def stdListToPyList(typename, list):
    '''
    Given std::list in gdb.Value, return a list of gdb.Value of the list's elements
    '''
    rslist = []
    nodes = StdListPrinter(typename, list).children()
    for (_, val) in iter(nodes):
        rslist.append(val)

    return rslist

