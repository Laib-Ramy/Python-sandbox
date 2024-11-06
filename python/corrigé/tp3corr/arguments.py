
def f1(foo, bar, /, arg):
    pass

def f2(a1, a2, a3=42, a4=5, /):
    pass

def f3(a1, a2, *, a3, a4):
    pass

def f4(foo, bar, /, a1, a2, *, a3, a4):
    pass

def f5(foo, bar, /, *args):
    return [foo, bar]+list(args)

def f6(*, a1=5, a2=6, **kwargs):
    d=dict(kwargs)
    d['a1']=a1
    d['a2']=a2
    return d

def f7(*args, **kwargs):
    return (len(args), len(kwargs))