import PyInstaller.__main__

PyInstaller.__main__.run([
    "TLSVersion.py",
    "--onefile",
    "--console",
    "--clean"
])