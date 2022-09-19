function gen_fib(n) {
    for (let i = 2; i < n; i++) {
        fib_arr.push(fib_arr[i-1] + fib_arr[i-2]);
    }
}

function outer(n) {
    fib_arr = [0,1]
    if (n == 0 || n == 1) {
        return fib_arr[n]
    }
    gen_fib(n)
    console.log(fib_arr)
    return fib_arr[fib_arr.length -1]
}

for (let i = 0; i < 10; i++) {
    console.log(i, outer(i))
}