#!/usr/bin/python3
"""Change comes from within.
"""


def makeChange(coins, total):
    """make change.
    """
    if total <= 0:
        return 0

    total_value = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        remain = (total-total_value)//coin
        total_value += remain*coin
        coin_used += remain
        if total_value == total:
            return coin_used
    return -1
