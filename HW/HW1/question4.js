function reversedSum(num1, num2) {
    num1 = num1.toString();
    num2 = num2.toString();
    num1 = num1.split("");
    num2 = num2.split("");
    
    while (num1[num1.length - 1] == '0') {
        num1.pop();
    }
    while (num2[num2.length - 1] == '0') {
        num2.pop();
    }

    var max_len = num1.length;
    if (num2.length > max_len) {
        max_len = num2.length;
    }

    var sum = 0;

    for (let i = 0; i < max_len; i++) {
        let temp_sum = 0;
        if (i < num1.length) {
            sum += parseInt(num1[i]) * Math.pow(10, i);
        }
        if (i < num2.length) {
            sum += parseInt(num2[i]) * Math.pow(10, i);
        }
    }

    sum = sum.toString();
    sum = sum.split("");
    while (sum[sum.length - 1] == '0') {
       sum.pop();
    }

    var reverse_sum = 0;
    for (let i = 0; i < sum.length; i++) {
        reverse_sum += sum[i] * Math.pow(10, i);
    }
    return reverse_sum;
}

console.log(reversedSum("24", 1));
console.log(reversedSum(4358, "754"));
console.log(reversedSum(305, 794));
