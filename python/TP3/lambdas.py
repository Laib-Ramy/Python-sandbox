
def is_multiple_of(n):
    return lambda x:x%n==0
    

def binary(op):
    return lambda x,y:eval(f'{x}{op}{y}')
