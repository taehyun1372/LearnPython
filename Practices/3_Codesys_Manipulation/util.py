import argsHandler
import json
import sys, os
from typing import Optional, Dict

from dacite import from_dict, Config

def get_arguments_instance(name = 'arguments.json'):
    try:
        with open(name, 'r') as f:
            data = json.load(f)
            # Convert a dictionary data into a class instance for better access in the code
            arguments = from_dict(data_class=argsHandler.Arguments, data=data, config=Config(cast=[Optional]))
            return arguments
    except Exception as e:
        print("Invalid JSON: {}".format(e))
        sys.exit(1)