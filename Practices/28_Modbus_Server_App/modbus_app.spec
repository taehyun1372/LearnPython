# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:\\Users\\a00533064\\OneDrive - ONEVIRTUALOFFICE\\Desktop\\Code\\LearnPython\\Practices\\28_Modbus_Server_App\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\a00533064\\OneDrive - ONEVIRTUALOFFICE\\Desktop\\Code\\LearnPython\\Practices\\28_Modbus_Server_App\\device.json', '.')],
    hiddenimports=['pymodbus', 'pymodbus.server.sync', 'pymodbus.datastore', 'pymodbus.transaction', 'pymodbus.framer.socket_framer', 'pymodbus.framer.ascii_framer', 'pymodbus.framer.rtu_framer', 'PyQt5', 'PyQt5.QtWidgets', 'PyQt5.QtGui', 'PyQt5.QtCore', 'qdarkstyle'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='modbus_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='modbus_app',
)
