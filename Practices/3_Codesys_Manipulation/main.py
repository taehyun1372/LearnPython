import subprocess
import util
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
    arguments = util.get_arguments_instance('arguments.json')
except Exception as e:
    print(f"Argument parsing failed..{e}")
    sys.exit(1)

# Argument serialization
dict = to_dict(arguments)
current_path = os.path.dirname(os.path.abspath(__file__))
temp_args_file = "arguments_temp.json"
temp_args_file_path = os.path.join(current_path, temp_args_file)

# Making a file with serialized argument data
try:
    with open(temp_args_file_path, "w") as f:
        json.dump(dict, f, indent=2)
except Exception as e:
    print(f"Failed to save the temporary arguments file..{e}")
    sys.exit(1)

codesys_path = arguments.files.codesysPath
project_path = os.path.join(arguments.files.projectPath, arguments.files.projectName)
codesys_version = arguments.files.codesysVersion
iron_python_script_path = os.path.join(current_path, arguments.files.ironPythonScript)

# Formatting command line
cmd = (
    f'cd {codesys_path} && '
    r'CODESYS.exe '
    r'--enablescripttracing '
    f'--project="{project_path}" '
    f'--profile="{codesys_version}" '
    f'--runscript="{iron_python_script_path}" '
    f"--scriptargs='{temp_args_file_path}'"
)

try:
    # Command line execution
    subprocess.run(cmd, shell=True)
except Exception as e:
    print(f"Failed to execute the command line..{e}")
    sys.exit(1)