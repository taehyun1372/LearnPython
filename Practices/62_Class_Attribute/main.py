class Config:
    def __init__(self):
        self.__id = "1234"
        self._path = "C"
        self.app = "DFS"
        
        
if __name__ == "__main__":
    config = Config()
    
    try:
        print(config.__id)
    except Exception:
        print("Could not get the attribute")
    print(config._path)
    print(config.app)
    
    try:
        print(getattr(config, "__id"))
    except:
        print("Could not get the attributes")
    print(getattr(config, "_path"))
    print(getattr(config, "app"))