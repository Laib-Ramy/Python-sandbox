
def is_multiple_of(n):
    return lambda x: x%n==0

def binary(op):
    return lambda a,b:eval(f'a {op} b')