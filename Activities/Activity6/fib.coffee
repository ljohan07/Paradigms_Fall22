fib = (n) ->
    n1 = 1
    n2 = 1
    sum = 0
    if n is 0
        return 0
    else if n is 1 or n is 2
        return 1
    else
        for i in [2...n]
            sum = n1 + n2
            console.log n1, n2, sum
            n1 = n2
            n2 = sum
    return sum

for i in [0...10]
    console.log 'fib', i, fib i
