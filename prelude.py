import sys
import os
def add_paths():
    pythondir = '/usr/share/gcc-8.3.0/python'
    print(f'add to the python sys.path: {pythondir}')
    sys.path.append(pythondir)
    scripts_folder = os.path.dirname(__file__)

    print(f'add to the python sys.path: {scripts_folder}')
    sys.path.append(scripts_folder)

add_paths()
