def fibgen(n=0):
    i1=0
    i2=1
    while True:
        if n and i2>n:
            return
        yield i2
        i1,i2 = i2, i1+i2