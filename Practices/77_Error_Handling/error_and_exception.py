# source : https://docs.python.org/ko/3/tutorial/errors.html
# while True
#     print("Hello world") # Syntax Error
 
# result = 10 * (1/0) # Zero division error

# 4 + spam * 3 # Name error

# '2' + 2 # Type error

# while True:
#     try:
#         x = int(input("Please enter a number"))
#         break
#     except (ValueError, RuntimeError, TypeError, NameError): # We can have a exception handling for multiple cause
#         print("Oops! That was no valid input. Try with numbers")


# def input_conversion(input):
#     return int(input) # This can be a value error

# if __name__ == "__main__":
#     try:
#         while True:
#             user_input = input("Please enter a input here >>")
#             try:
#                 result = input_conversion(user_input)
#                 break
#             except ValueError:
#                 print("Failed to convert, I know what to do")

#     except Exception as ex:
#         print("This is application safe net. I didn't know it can happen. I will find out how to handle it", ex)


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")    
    except C:
        print("C")    
    except B:
        print("B") # parent exception catches all children

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B") # parent exception catches all children
    except C:
        print("C")    
    except D:
        print("D")

try:
    raise Exception("spam", "eggs")
except Exception as inst:
    print(type(inst))
    print(type(inst.args))
    print(inst)

    x, y = inst.args
    print(f"x = {x}")
    print(f"y = {y}")



# def file_read(path):
#     try:
#         f = open(path)
#         s = f.readline()
#         i = int(s.strip())
#     except OSError as err:
#         print("OS error ", err)
#         raise
#     except ValueError:
#         print("Could not conver data into an integer")
#         raise

# try:
#     while True:
#         try:
#             path = input("Type desired path here>> ")
#             file_read(path)
#             break
#         except (OSError, ValueError):
#             print("I know the context. I know what to do")
# except Exception as err:
#     print(f"Application safe net {err=}, {type(err)=}")

raise NameError("Hi There")
