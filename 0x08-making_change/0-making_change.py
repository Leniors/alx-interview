#!/usr/bin/python3
"""
makeChange function file
"""

def makeChange(coins, total):
    """ makeChange function """
    if total <= 0:
        return 0
    
    if total in coins:
        return 1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # coins.sort()
    
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
