import pickle
import base64
import sys
import StringIO

class SimpleNamespace(object):
    pass

class SafeUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Return a simple container instead of the original class
        return SimpleNamespace

if __name__ == "__main__":
    max = int(sys.argv[1])
    total = ""
    for i in range(max):
        total += sys.argv[i+2]

    decoded = base64.b64decode(total)
    unpickler  = SafeUnpickler(io.BytesIO(decoded))
    arguments = unpickler.load()

    print(arguments.target.deviceName)  # prints "project1"
    print(arguments.projectFile.backupXMLName)  # prints "my_path"