#!/usr/bin/python3
"""
Task 0. Change comes from within

Determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """makeChange

    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    Arguments:
        coins (List): A list (pile) of coins of different values.
        total (int): The total needed.

    Return:
        (int): The minimum number of coins needed to meet the total.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    coins.sort()

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
