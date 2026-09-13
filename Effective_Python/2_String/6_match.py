def take_action(light):
    if light == "red":
        print("stop")
    elif light == "yellow":
        print("slow down")
    elif light == "green":
        print("go")
    else: raise RuntimeError

take_action("red")
take_action("yellow")
take_action("green")

def take_match_action(light):
    match light:
        case "red":
            print("stop")
        case "yellow":
            print("slow down")
        case "green":
            print("green")
        case _:
            raise RuntimeError

take_match_action("red")
take_match_action("yellow")
take_match_action("green")

RED = "red"
YELLOW = "yellow"
GREEN = 'green'

# def take_match_action2(light):
#     match light:
#         case RED:
#             print("stop")
#         case YELLOW:
#             print("slow down")
#         case GREEN:
#             print("green")
#         case _:
#             raise RuntimeError

# take_match_action2("red")
# take_match_action2("yellow")
# take_match_action2("green")

def take_debug_action(light):
    match light:
        case RED:
            print(f"{RED}, {light}")

take_debug_action(GREEN)

import enum

class ColorEnum(enum.Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"

def take_enum_action(light):
    match light:
        case ColorEnum.RED:
            print("stop")
        case ColorEnum.YELLOW:
            print("slow down")
        case ColorEnum.GREEN:
            print("go")
        case _:
            raise RuntimeError

take_enum_action(ColorEnum.RED)
take_enum_action(ColorEnum.YELLOW)
take_enum_action(ColorEnum.GREEN)

if ColorEnum.RED == "red":
    print("Red is red")