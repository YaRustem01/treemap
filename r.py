class R:
    def __init__(self, x, y, w, h, v=0.0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = v

    def __str__(self):
        return f"({self.x}, {self.y}) [{self.w}:{self.h}]={self.v}"

    @property
    def orig(self):
        return (self.x, self.y)

    @property
    def size(self):
        return (self.w, self.h)

    @property
    def area(self):
        return self.w * self.h
