

def collatz(n):
    while True:
        yield n
        if n==1:
            return
        n = 3*n+1 if n%2 else n//2

def collatz_list(n):
    return [i for i in collatz(n)]

def collatz_set(n):
    return {i for i in collatz(n)}

def collatz_dict(n):
    return {i:[k for k in collatz(i)] for i in range(1,n+1)}

def collatz_count(n):
    return sum(1 for _ in collatz(n))