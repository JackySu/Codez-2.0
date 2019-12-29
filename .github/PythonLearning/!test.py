class Student(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
print(s.age())

# line 5 如果直接写 return 25，输出的时候能直接print(s.age) 但是lambda（即一个匿名函数）将其变成了方法
# 方法（除了特殊方法）肯定要加括号
# __str__也是一个方法，但是比较特殊，不用加括号
# 当我print(s.age)的时候调用的是属性，但这个age属性不存在就会直接问__getattr__要结果
# 最后，到return 该函数即结束
