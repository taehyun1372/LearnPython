from pathlib import Path

class LogManager:
    def __init__(self, path):
        self.__path = path
        self.__default_path = Path.joinpath(Path(__file__).parent, "log.txt") 

    def add_log(self, message):
        with open(self.__path, "a") as file:
            file.write(message + "\n")

    def read_log(self):
        result = []

        if Path(self.__path).exists():
            path = self.__path
        else:
            raise FileNotFoundError('Cannot find the log file ', self.__path)

        with open(path, "r") as file:
            for line in file.readlines():
                result.append(line)
                print(line, end="")

        return result


if __name__ == "__main__":
    try:
        path = Path.joinpath(Path(__file__).parent, "log1.txt") 
        log = LogManager(path)
        # log.add_log("Info,2026-09-27 11:02:00,Temporary Stop")
        print("task 1")
        result = log.read_log()
        print(result)
        print("Another task 2")
        print("Another task 3")
    except Exception as ex:
        print("Exception occurred ", ex)
