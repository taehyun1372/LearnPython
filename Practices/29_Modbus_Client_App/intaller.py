import subprocess
import sys
from pathlib import Path
import platform

PROJECT_DIR = Path(__file__).parent
MAIN_FILE = PROJECT_DIR / "main.py"
DATA_FILE = PROJECT_DIR / "device.json"

DIST_NAME = "modbus_client_app"

# OS-specific separator
DATA_SEP = ";" if platform.system() == "Windows" else ":"

HIDDEN_IMPORTS = [
    # pymodbus
    "pymodbus",
    "pymodbus.server.sync",
    "pymodbus.datastore",
    "pymodbus.transaction",
    "pymodbus.framer.socket_framer",
    "pymodbus.framer.ascii_framer",
    "pymodbus.framer.rtu_framer",

    # PyQt5
    "PyQt5",
    "PyQt5.QtWidgets",
    "PyQt5.QtGui",
    "PyQt5.QtCore",

    # qdarkstyle
    "qdarkstyle",
]

def build():
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconsole",
        "--onedir",
        f"--name={DIST_NAME}",
        f"--add-data={DATA_FILE}{DATA_SEP}.",
    ]

    for module in HIDDEN_IMPORTS:
        cmd.append(f"--hidden-import={module}")

    cmd.append(str(MAIN_FILE))

    print("Running PyInstaller...")
    subprocess.run(cmd, check=True)

    print("\nBuild complete!")
    print(f"Output: dist/{DIST_NAME}/")

if __name__ == "__main__":
    build()
