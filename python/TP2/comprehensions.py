

def collatz(n):
    while True:
        yield n
        if n==1:
            return
        n = 3*n+1 if n%2 else n//2

def collatz_list(n):
    pass

def collatz_set(n):
    pass

def collatz_dict(n):
    pass

def collatz_count(n):
    pass