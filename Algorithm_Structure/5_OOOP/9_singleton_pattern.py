class SinEx:
    _sing = None

    def __new__(cls, *args, **kwargs):
        if cls._sing is None:
            cls._sing = super().__new__(cls)

        return cls._sing

    def __init__(self, name):
        if hasattr(self, "_initialized"):
            return

        self.name = name
        self._initialized = True

    def print_name(self):
        print(f"{self.name} is unique object")

if __name__ == "__main__":
    roy = SinEx("Roy")
    print(roy)
    roy.print_name()

    taehyun = SinEx("Teahyun")
    print(taehyun)
    taehyun.print_name()