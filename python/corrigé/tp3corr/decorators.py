from random import random

def keep_calm(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return None
    return wrapper

def insist(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception:
                pass
    return wrapper



def bad_function():
    if random()<0.1:
        return 42
    raise Exception('This is kind of normal for this function to fail')

@keep_calm
def calm_function():
    return bad_function()

@insist
def good_function():
    return bad_function()