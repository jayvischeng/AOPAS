# -*- mode: python -*-
a = Analysis(['Ui_MainWindow.py'],
             pathex=['F:\\EricPython2'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Ui_MainWindow.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='F:\\EricPython2\\title.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='Ui_MainWindow')
