class C:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, value):
    #     if type(value) == str:
    #         self._name = value
    #     else:
    #         raise ValueError

if __name__ == "__main__":
    c = C("roy")
    print(c.name)
    c.name = "Roy"
    print(c.name)
    c.name = 123
    print(c.name)
    