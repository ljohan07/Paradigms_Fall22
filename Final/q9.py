import math
class Votes:
    def __init__(self,v):
      self.v = v

    def __add__(self, v):
        return self.v + v.v
    def __sub__(self, v):
        return self.v - v.v
    def __ge__(self, v):
        return self.v >= v.v
    def __le__(self, v):
        return self.v <= v.v
    def __gt__(self, v):
        return self.v > v.v
    def __lt__(self, v):
        return self.v < v.v
    def __eq__(self, v):
        return self.v == v.v


if __name__ == '__main__':
    v1 = Votes(12)
    v2 = Votes(5)
    v3 = Votes(12)
    assert v1+v2 == 17
    assert v1-v2 == 7
    assert (v1>=v2) == True
    assert (v1<=v2) == False
    assert (v1>v2) == True
    assert (v1<v2) == False
    assert(v1==v2) == False
    assert (v1==v3) == True