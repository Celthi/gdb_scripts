import sys
import os
def add_paths(file_name):
    scripts_folder = os.path.dirname(file_name)
    print('add to the python sys.path: '+ scripts_folder)
    sys.path.insert(0, scripts_folder)

add_paths(__file__)
