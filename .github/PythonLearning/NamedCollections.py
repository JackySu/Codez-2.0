from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 1)
print(p.x, p.y)


q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key2'])


od = OrderedDict([('a', 1), （'b', 2), ('c', 3)])
print(od)
# od会按照插入的顺序排列，跟栈同理

