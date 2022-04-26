"""
Get the path of files in the same folder with this GH file.
If filename is omitted, this will return the path of this GH file.

Please configure the Grasshopper component's parameters as the following:
Input:
    - filename: list_access, type_hint: str
Output:
    - path
    - file
"""

import Grasshopper
import os

filepath = ghenv.Component.OnPingDocument().FilePath
path = os.path.dirname(filepath)
if filename:
    path = os.path.join(path, *filename)


file = None
if os.path.isfile(path):
    with open(path) as f:
        file = f.readlines()
