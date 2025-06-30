import base64
import subprocess
import Util
import sys
import json
import os

def to_dict(obj):
    if hasattr(obj, "__dict__"):
        result = {}
        for key, val in obj.__dict__.items():
            result[key] = to_dict(val)
        return result
    elif isinstance(obj, (list, tuple, set)):
        return [to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {to_dict(k): to_dict(v) for k, v in obj.items()}
    else:
        # Base case: primitive types (str, int, float, bool, None)
        return obj

# Argument processing
try:
    print("Argument parsing started..")
    arguments = Util.get_arguments_instance('test_arguments.json')

except Exception as e:
    print(f"Argument parsing failed..{e}")
    sys.exit(1)

# Serialization
dict = to_dict(arguments)
current_path = os.path.dirname(os.path.abspath(__file__))
temp_file_name = "temp.json"
full_path = os.path.join(current_path, temp_file_name)

with open(full_path, "w") as f:
    json.dump(dict, f, indent=2)

cmd = (
    r'cd "C:\Program Files (x86)\CODESYS 3.5.20.50\CODESYS\Common" && '
    r'CODESYS.exe '
    r'--project="C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\Modbus_Test_Project.project" '
    r'--profile="CODESYS V3.5 SP20 Patch 5" '
    r'--runscript="C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\codesysHandler.py" '
)

args = f"--scriptargs='{full_path}'"

subprocess.run(cmd + args, shell=True)