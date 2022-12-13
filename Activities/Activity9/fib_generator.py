def fib_gen(n):
    fib_curr = 0
    fib_next = 1
    while n > 0:
        yield fib_next
        n -= 1
        new_next = fib_curr + fib_next
        fib_curr = fib_next
        fib_next = new_next


print(list(fib_gen(5)))