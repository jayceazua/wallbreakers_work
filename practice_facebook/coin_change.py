"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""


def coinChange(coins, amount):
    def _coinChange(coins, rem, count):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if count[rem - 1] != 0:
            return count[rem - 1]
        minCost = float('inf')

        for coin in coins:
            res = _coinChange(coins, rem - coin, count)

            if res >= 0 and res < minCost:
                minCost = 1 + res

        if minCost == float('inf'):
            count[rem - 1] = -1
        else:
            count[rem - 1] = minCost

        return count[rem - 1]
    if amount < 1:
        return 0
    count = [0]*amount
    return _coinChange(coins, amount, count)


# DP bottom/up
def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)

    return dp[-1] if dp[-1] != float('inf') else -1
