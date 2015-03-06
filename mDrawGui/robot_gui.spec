# -*- mode: python -*-

block_cipher = None


a = Analysis(['robot_gui.py'],
             pathex=['E:\\robot_python\\ScaraGui'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='robot_gui.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='mDraw.ico')
