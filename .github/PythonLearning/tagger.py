import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('process result: ')
        func(*args, **kwargs)
        return func

    return wrapper


@decorator
def tagger(cont):
    print('<' + cont + '>')


raw = str(input())
tagger(raw)
