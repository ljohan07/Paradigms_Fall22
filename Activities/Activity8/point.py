import math
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print(self):
        print('(' + str(self.x) + ',' + str(self.y) + ')')
def distance(p1, p2):
    return math.sqrt(math.pow((p1.x-p2.x), 2) + math.pow((p1.y-p2.y), 2))