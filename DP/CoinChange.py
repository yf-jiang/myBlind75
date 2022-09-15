def coinChange(coins, amount):
    dpArr = [0] + [amount + 1] * amount

    for a in range(1, amount + 1):
        for coin in coins:
            if (a - coin) >= 0:
                dpArr[a] = min(1 + dpArr[a - coin], dpArr[a])

    if dpArr[amount] != amount + 1:
        return dpArr[amount]

    else:
        return -1


coins1 = [1, 2, 5]
amount1 = 11
coins2 = [2]
amount2 = 3
coins3 = [1]
amount3 = 0

print(coinChange(coins1, amount1))
print(coinChange(coins2, amount2))
print(coinChange(coins3, amount3))
