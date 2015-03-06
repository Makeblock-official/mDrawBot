from distutils.core import setup
import py2exe

py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll","QtCore4.dll","QtGui4.dll","QtNetwork4.dll"],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 1,
        }

setup(windows=[{"script":"robot_gui.py","icon_resources": [(1, "mDraw.ico")]}],options={'py2exe': py2exe_options},zipfile = None)