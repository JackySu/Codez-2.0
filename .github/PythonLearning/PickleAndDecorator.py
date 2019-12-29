# import numpy as np

# a = np.array([2, 3, 4])
# print(a, a.dtype)

'''
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        end = time.time()
        print(f'task {func.name} runs for {end - start - 1:0.2f}')
        return func

    return wrapper
'''
# codes above wont work due to transmission between process needs to be
# SERIALIZED, the solution is to change function decorator to class decorator

# example is as follows

import random
import multiprocessing
import functools


class my_decorator(object):
    def __init__(self, target):
        self.target = target
        try:
            functools.update_wrapper(self, target)
        except:
            pass

    def __call__(self, candidates, args):
        f = []
        for candidate in candidates:
            f.append(self.target([candidate], args)[0])
        return f


def old_my_func(candidates, args):
    f = []
    for c in candidates:
        f.append(sum(c))
    return f


my_func = my_decorator(old_my_func)

if __name__ == '__main__':
    candidates = [[random.randint(0, 9) for _ in range(5)] for _ in range(10)]
    pool = multiprocessing.Pool(processes=4)
    results = [pool.apply_async(my_func, ([c], {})) for c in candidates]
    pool.close()
    f = [r.get()[0] for r in results]
    print(f)
