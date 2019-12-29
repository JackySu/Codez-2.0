class Animal(object):
    def __init__(self, name):
        self.__name = name

    def run(self):
        print("%s is running" % self.__name)


class Dog(Animal):
    pass


dog = Dog("Harley")
dog.run()
