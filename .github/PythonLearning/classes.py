import re


class Student(object):

    # def __init__(self, name, gender, score):
    #     self._name = name
    #     self._gender = gender
    #     self._score = score

    def __str__(self):
        return 'Student status %s, %s, %s' % (self._name, self._gender, self._score)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must be within 0 ~ 100")
        self._score = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.isalnum:
            value.replace(" ", "")

        if re.match(r'[a-zA-Z]{1,20}$', value):
            self._name = value
        else:
            print("input name illegal, should be 1~20 characters long w/ out number")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    def print_data(self):
        print("%s: %s" % (self._name, self._gender))


Stu01 = Student()
Stu01.name = input("Enter name")
