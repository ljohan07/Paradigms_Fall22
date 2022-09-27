changeEnough =   (changeInPocket, amount)  ->
    total_money = 25 * changeInPocket[0] + 10 * changeInPocket[1] + 5 * changeInPocket[2] + changeInPocket[3]
    return total_money >= amount * 100

module.exports = { changeEnough }
