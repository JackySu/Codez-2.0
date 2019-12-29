class Chain:

    def __init__(self, path=''):  # path cant be None
        self._path = path

    def __getattr__(self, path):
        if path == "users":
            # GET /users/:user/repos
            return lambda x: Chain('/users/%s' % x)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)  # /status/user/timeline/list
print(Chain().users('michael').repos)  # /users/michael/repos

# 带括号一定是个方法（包括初始化一个实例也是）方法不一定带括号（特殊的方法比如__str__ __call__）
# Step 1 Chain()初始化一个实例 path=''（啥都没有）
# Step 2 查找urls的属性users，没有查到，调用getattr，，再返回一个Chain(...)，把要查找的users作为参数传进去
# Step 3 urls = urls('michael')
# 函数本身是可调用对象，类本身也是，如生成实例化对象，但类实例化的对象没加call就不可以被调用，纯粹是个对象而已
# str主要是返回这个实例内部重要数据
