import argsHandler
import XMLHandler
import json
from typing import Optional, Dict
from dataclasses import dataclass, asdict
import sys
import Util
from XMLHandler import XMLHandler





# Argument processing
try:
    print("Argument parsing started..")
    arguments = Util.get_arguments_instance()

except Exception as e:
    print(f"Argument parsing failed..{e}")
    sys.exit(1)

# XML processing
try:
    print("Initialising xml handler started..")
    xmlHandler = XMLHandler(arguments)

except Exception as e:
    print(f"Initialising xml handler failed..{e}")
    sys.exit(1)

xmlHandler.process()



