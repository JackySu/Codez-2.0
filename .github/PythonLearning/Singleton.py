class Singleton:

    __obj = None
    __init_flag = True

    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = super().__new__(cls)
        return cls.__obj

    def __init__(self, name):
        if Singleton.__init_flag:
            print("initializing...")
            self.name = name
            Singleton.__init_flag = False


a = Singleton("aa")
b = Singleton("bb")
print(a)
print(b)
