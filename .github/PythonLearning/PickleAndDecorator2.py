from multiprocessing import Pool
import functools
import time


def decorate_func(func):
    functools.wraps(func)

    def _decorate_func(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        time.sleep(0.1)
        timer = time.time() - start - 0.1
        print(f'Process {func.__name__} processed for {timer}')
        return ret

    return _decorate_func


def actual_func(x):
    return x**2


def wrapped_func(*args, **kwargs):
    return decorate_func(actual_func)(*args, **kwargs)


if __name__ == '__main__':
    my_swimming_pool = Pool()
    result = my_swimming_pool.apply_async(wrapped_func, (2, ))
    print(result.get())
