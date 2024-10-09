from random import random

def keep_calm(func):
    def wrap(*args,**kwargs):
        try :
            rv=func(*args,**kwargs)
            return rv
        except :
            return None
    return wrap       

def insist(func):
    def wrap(*args,**kwargs):
        while True :
            try :
                return func(*args,**kwargs)
            except:
                pass
                
    return wrap



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