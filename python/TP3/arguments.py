
def f1(a,b,/,arg):
    pass

def f2(a,b,c=42,d=5,/):
    pass

def f3(a1,a2,*,a3,a4):
    pass

def f4(b1,b2,/,a1,a2,*,a3,a4):
    pass

def f5(x,y,/,*args):
    return [x,y]+list(args)

def f6(*,a1=5,a2=6,**kwargs):
    kwargs['a1']=a1
    kwargs['a2']=a2
    return kwargs

def f7(*args,**kwargs):
    return (len(args),len(kwargs))
    