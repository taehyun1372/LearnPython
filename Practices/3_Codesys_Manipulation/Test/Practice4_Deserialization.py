import pickle
import base64
import subprocess
import sys
from types import SimpleNamespace
import io

class SafeUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Return a simple container instead of the original class
        return SimpleNamespace

if __name__ == "__main__":
    encoded = sys.argv[1]
    decoded = base64.b64decode(encoded)
    obj = SafeUnpickler(io.BytesIO(decoded)).load()

    print(obj.name)  # prints "project1"
    print(obj.age)  # prints "my_path"


