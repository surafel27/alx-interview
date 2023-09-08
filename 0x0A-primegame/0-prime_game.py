#!/usr/bin/python3
"""PrimeGame Module.
"""


def isWinner(x, nums):
    """prime game."""
    if not nums or x < 1:
        return None
    marias_wins = 0
    bens_wins = 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for _, num in zip(range(x), nums):
        prime_count = len(list(filter(lambda x: x, primes[0:num])))
        bens_wins += prime_count % 2 == 0
        marias_wins += prime_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return "Maria" if marias_wins > bens_wins else "Ben"
