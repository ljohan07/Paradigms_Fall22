import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print(self):
        print('(' + str(self.x) + ',' + str(self.y) + ')')
    def distance(self, p2):
        return math.sqrt(math.pow((self.x-p2.x), 2) + math.pow(((self).y-p2.y), 2))
    def __gt__(self, p2):
        origin = Point(0,0)
        dist1 = origin.distance(self)
        dist2 = origin.distance(p2)
        return dist1 > dist2
    def __ge__(self, p2):
        origin = Point(0,0)
        dist1 = origin.distance(self)
        dist2 = origin.distance(p2)
        return dist1 >= dist2
    def __eq__(self, p2):
        origin = Point(0,0)
        dist1 = origin.distance(self)
        dist2 = origin.distance(p2)
        return dist1 == dist2
    def __lt__(self, p2):
        origin = Point(0,0)
        dist1 = origin.distance(self)
        dist2 = origin.distance(p2)
        return dist1 < dist2
    def __le__(self, p2):
        origin = Point(0,0)
        dist1 = origin.distance(self)
        dist2 = origin.distance(p2)
        return dist1 <= dist2



p1 = Point(2,3)
p2 = Point(-3,1)
p3 = Point(-2,-3)
print(p1 > p2) # = True # p1 is more distant to the origin than p2
print(p1 == p2) # = False # p1 and p2 are not equally distant to the origin 
print(p1 < p2) # = False # p1 is not closer to the origin as compared to p2
print(p1 == p3) # = True