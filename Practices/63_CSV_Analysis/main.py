import csv
from pathlib import Path

script_dir = Path(__file__).resolve().parent
folder = Path.joinpath(script_dir, "data")


for path in folder.rglob("*"):
    print(path)
