function parityAnalysis(n){
    num_sum = getDigitSum(n)
    if ((n % 2 == 1 && num_sum % 2 == 1) || (n % 2 == 0 && num_sum % 2 == 0)) {
        return true
    }
    else {
        return false
    }
}

function getDigitSum(n) {
    sum = 0
    while (n > 0) {
        sum += n % 10
        n /= 10
        n = Math.floor(n)
    }
    return sum
}

// console.log(parityAnalysis(243))
// console.log(parityAnalysis(12))
// console.log(parityAnalysis(3))
// console.log(parityAnalysis(552555))
module.exports = {parityAnalysis}