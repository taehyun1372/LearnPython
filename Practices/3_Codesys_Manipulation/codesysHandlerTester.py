import pickle
import base64
import subprocess
import Util
import sys

# Argument processing
try:
    print("Argument parsing started..")
    arguments = Util.get_arguments_instance()

except Exception as e:
    print(f"Argument parsing failed..{e}")
    sys.exit(1)

# Serialization
serialized = pickle.dumps(arguments)
encoded = base64.b64encode(serialized).decode("utf-8")  # base64 -> string
list_of_args = []
max = int(len(encoded) / 200)
for i in range(max):
    list_of_args.append(encoded[i*200:(i+1)*200])


cmd = (
    r'cd "C:\Program Files (x86)\CODESYS 3.5.20.50\CODESYS\Common" && '
    r'CODESYS.exe '
    r'--project="C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\Modbus_Test_Project.project" '
    r'--profile="CODESYS V3.5 SP20 Patch 5" '
    r'--runscript="C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\codesysHandlerTestee.py" '
)


args = f"--scriptargs='{max} {list_of_args[0]} {list_of_args[1]} {list_of_args[2]} {list_of_args[3]} {list_of_args[4]} {list_of_args[5]} {list_of_args[6]} {list_of_args[7]} {list_of_args[8]} {list_of_args[9]} {list_of_args[10]}'"

subprocess.run(cmd + args, shell=True)