

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __eq__(self, p):
        return self.x==p.x and self.y==p.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'point.Point({self.x}, {self.y})'
