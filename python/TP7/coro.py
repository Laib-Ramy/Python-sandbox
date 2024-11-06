
# This is a decorator intended to start the coroutine by calling next()
def coroutine(func):
    def starter(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return starter


@coroutine
def running_average():
    pass