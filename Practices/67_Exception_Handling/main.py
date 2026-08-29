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
        # We explicitly print traceback
        traceback.print_exc()

def process_manager(path, status = "normal"):
    # Wether we can proceed or not depends on the system status. 
    if status == "normal":
        print_content_explicit_print(path)
    else:
        print_content_bare_try(path)

if __name__ == "__main__":
    print("Process 1")
    print("Process 2")
    process_manager("data\\log1.txt", "alarm") # Target handling process
    print("Process 4")
    print("Process 5")
