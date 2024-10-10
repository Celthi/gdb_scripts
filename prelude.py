import sys
import os
def add_paths():
    pythondir = '/usr/share/gcc/python'
    print('add to the python sys.path: '+ pythondir)
    sys.path.append(pythondir)
    scripts_folder = os.path.dirname(__file__)

    print('add to the python sys.path: '+ scripts_folder)
    sys.path.insert(0, scripts_folder)

add_paths()
