class A2:
    def say(self):
        print('a2 says..')


class B2:
    def __init__(self, a):
        self.a = a


a2 = A2()
b2 = B2(a2)
b2.a.say()
