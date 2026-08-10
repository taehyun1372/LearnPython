import io
import traceback

# Potentially failling function
def print_content_bare_try(path):
    # Unhandled exception noramlly produces traceback message
    # FileNotFoundError: [Errno 2] No such file or directory: 'data\\log1.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)

# 
def print_content_silent_fail(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    except:
        # We catch the exception so it doesn't reach to the python default exception handler which prints traceback
        pass

def print_content_explicit_print(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
    except:
        traceback.print_exc()

if __name__ == "__main__":
    print("Process 1")
    print("Process 2")
    print_content_bare_try("data\\log1.txt") #target handling process
    print("Process 4")
    print("Process 5")
