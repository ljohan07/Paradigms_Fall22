class move_robot:
    def __init__(self, n):
        self.m = -1
        self.n = n
        self.pos = [0,0]


    def __iter__(self): # creates iterable object
        return self


    def __next__(self): # invoked at every iteration
        while self.m < self.n:
            if self.m == -1:
                self.m += 1
                return tuple(self.pos)
            
            face = (self.m) % 4
            if face == 0:
                # move north
                self.pos[1] += (self.m + 1)
            elif face == 1:
                # move east
                self.pos[0] += (self.m + 1)
            elif face == 2:
                # move south
                self.pos[1] -= (self.m + 1)
            else:
                # move west
                self.pos[0] -= (self.m + 1)
            self.m += 1
            #print(self.pos)
            return tuple(self.pos)
        else:
            raise StopIteration()