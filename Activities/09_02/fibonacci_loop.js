function fibonacci(n){
    if (n == 0) {
        return 0;
    }
    fib = [0, 1];
    var temp_sum = 0;
    for (i = 1; i < n; i++) {
        temp_sum = fib[0] + fib[1];
        fib[0] = fib[1];
        fib[1] = temp_sum;
    }
    return fib[1];
}
