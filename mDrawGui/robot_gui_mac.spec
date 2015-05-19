# -*- mode: python -*-
import os

a = Analysis(['robot_gui.py'],
             pathex=['/Users/RivenYeung/robot_python/ScaraGui'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
a.datas += [
     ('avrdude',os.getcwd()+'/avrdude','DATA'),
     ('potrace',os.getcwd()+'/potrace','DATA'),
     ('avrdude.conf',os.getcwd()+'/avrdude.conf','DATA'),
     ('XY.hex',os.getcwd()+'/XY.hex','DATA'),
     ('mScara.hex',os.getcwd()+'/mScara.hex','DATA'),
     ('mSpider.hex',os.getcwd()+'/mSpider.hex','DATA'),
     ('mEggBot.hex',os.getcwd()+'/mEggBot.hex','DATA'),
     ('mCar.hex',os.getcwd()+'/mCar.hex','DATA'),
     ]
print "\n\n#### package ####",a.datas
print "\n\n"

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='robot_gui',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='mDraw.icns')
app = BUNDLE(exe,
             name='mDraw.app',
             icon='mDraw.icns')
