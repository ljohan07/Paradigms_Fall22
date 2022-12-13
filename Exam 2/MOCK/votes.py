import math
class Votes:
    def __init__(self,v):
      self.v = v
    def __add__(self, v2):
        return self.v + v2.v

v1 = Votes(5)
v2 = Votes(12)
print(v1+v2)
assert(v1+v2 == 17)