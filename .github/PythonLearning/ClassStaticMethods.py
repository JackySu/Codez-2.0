class A:
    def foo1(self):
        print("i am obj", self)

    @staticmethod
    def foo2():
        print("im static")

    @classmethod
    def foo3(cls):
        print("im classM", cls)
        cls().foo2()


a = A()
A.foo1(a)  # equivalent to a.foo1()
A.foo2()
a.foo3()  # equivalent to A.foo3() or A().foo3()
