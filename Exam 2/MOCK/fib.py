import sys
class fibonacci():
    def __init__(self, n):
        self.curr = 0
        self.next = 1
        self.tracker = n

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.tracker == 0:
            raise StopIteration()
        else:
            new_next = self.curr + self.next
            self.curr = self.next
            self.next = new_next
            self.tracker -= 1
            return self.curr

if __name__ == '__main__':
    num = int(sys.stdin.readline())
    a = fibonacci(num)
    for obj in a:
        print(obj)
# a = fibonacci(5)
# for obj in a:
#     print(obj)