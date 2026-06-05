import subprocess

subprocess.run([
    "pyinstaller",
    "--onedir",
    "--windowed",
    "--add-data", "config.json;.",
    "--add-data", "BatchLabel_Material.zpl;.",
    "main.py"
])