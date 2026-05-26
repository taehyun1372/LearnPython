import os

ABS_PATH_1 = r"C:\Temp\Logs.txt"
ABS_PATH_2 = "C:\\Users\\ko1z528\\OneDrive - Kohler Co\\바탕 화면\\Code\\LearnPython\\Practices\\48_Path\\Logs.txt"
REL_PATH_1 = "Logs.txt"

def file_read(path):
    with open(path, "r") as f: # Absolute Path
        return f.read()

def get_current_working_directory():
    return os.getcwd()

def split_directory_name(path):
    return os.path.dirname(path)

def split_file_name(path):
    return os.path.basename(path)

def join_path(dir, file):
    return os.path.join(dir, file)


def get_script_directory():
    return os.path.abspath(__file__)

def get_script_base_directory():
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    print(get_current_working_directory())
    
    basepath = split_directory_name(ABS_PATH_2)
    filename = split_file_name(ABS_PATH_2)
    fullpath = join_path(basepath, filename)
    
    print(basepath)
    print(filename)
    print(fullpath)
    
    print(get_script_directory())
    print(get_script_base_directory())
    
    if (os.path.exists(fullpath)):
        content = file_read(fullpath)
        print(content)
    
    
    




