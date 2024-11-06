

class Fib:
    def __init__(self, n=0):
        self.n=n

    def __iter__(self):
        return FibIterator_(self.n)

    def __contains__(self, k):
        if k<=0:
            return False
        else:
            for m in self:
                if m>=k:
                    break
        return m==k


class FibIterator_:
    def __init__(self, n):
        self.n=n
        self.count_=0
        self.i1_=1
        self.i2_=0

    def __next__(self):
        self.count_+=1
        if self.n and self.count_>self.n:
            raise StopIteration
        self.i1_,self.i2_=self.i2_, self.i1_+self.i2_
        return self.i2_