class Device1:
    def __init__(self):
        self.name = "device 1"
    
    def method_1(self):
        return self.name + " method 1"
    
    def method_2(self):
        return self.name + " method 2"
    
    def method_3(self):
        return self.name + " method 3"
    
class Device2:
    def __init__(self):
        self.name = "device 2"
    
    def method_1(self):
        return self.name + " method 1"
    
    def method_2(self):
        return self.name + " method 2"
    
    def method_3(self):
        return self.name + " method 3"
    
if __name__ == "__main__":
    device1 = Device1()
    device2 = Device2()
    devices = {"Device1": device1, "Device2": device2}
    
    parameters = {"Device1": "method_1", "Device2": "method_3"}
    for k, v in parameters.items():
        device = devices.get(k)
        if device:
            cmd = getattr(device, v)
            if cmd:
                result = cmd()
                print(result)