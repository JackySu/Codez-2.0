import requests
import functools
import time
from multiprocessing import Pool


class timer(object):
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args):
        start = time.time()
        ret = self.func(*args)
        time.sleep(0.1)
        # if doesn't sleep the runtime would be 0.0
        return ret, f'process {self.func.__name__} run in {time.time() - start - 0.1}'


def get(url):
    return requests.get(url)


timer_get = timer(get)

if __name__ == '__main__':
    pool = Pool()
    url = 'https://' + input() + '/'
    result = pool.apply_async(timer_get, (url, ))
    print(result.get())
