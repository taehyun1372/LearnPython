import pickle
import base64
import subprocess

class Address:
    def __init__(self, city, zipcode):
        self.city = city
        self.zipcode = zipcode

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

if __name__ == "__main__":
    addr = Address("Seoul", 12345)
    person = Person("Roy", 22, addr)

    serialized = pickle.dumps(person)
    encoded = base64.b64encode(serialized).decode("utf-8")  # base64 -> string

    cmd = (
        r'start "" cmd /k "'
        r'"C:\Program Files\Python37\python.exe" '
        r'"C:\Users\a00533064\OneDrive - ONEVIRTUALOFFICE\Desktop\Code\LearnPython\Practices\3_Codesys_Manipulation\Test\Practice4_Deserialization.py" '
        rf'{encoded}"'
    )

    subprocess.run(cmd, shell=True)
