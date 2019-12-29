def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('execute')  # now = log('execute')
def now():
    print('2015-3-25')


now()
