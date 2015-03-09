# -*- mode: python -*-
import os

block_cipher = None


a = Analysis(['robot_gui.py'],
             pathex=['E:\\robot_python\\ScaraGui'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)

a.datas += [
     ('avrdude.exe',os.getcwd()+'/avrdude.exe','DATA'),
     ('potrace.exe',os.getcwd()+'/potrace.exe','DATA'),
     ('avrdude.conf',os.getcwd()+'/avrdude.conf','DATA'),
     ('XY.hex',os.getcwd()+'/XY.hex','DATA'),
     ('mScara.hex',os.getcwd()+'/mScara.hex','DATA'),
     ('mSpider.hex',os.getcwd()+'/mSpider.hex','DATA'),
     ('mEggBot.hex',os.getcwd()+'/mEggBot.hex','DATA'),
     ('mCar.hex',os.getcwd()+'/mCar.hex','DATA'),
     ]
print "\n\n#### package ####",a.datas
print "\n\n"

             
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mDraw.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='mDraw.ico')
