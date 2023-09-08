#!/usr/bin/python3
'''prime game'''


def isWinner(x, nums):
    '''define a function to check for prime number'''
    def is_prime(num):
        '''check is a number is prime'''
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_round(n):
        '''these is a play ground'''
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        dp = [False] * (n + 1)
        dp[0] = False
        dp[1] = False

        for i in range(2, n + 1):
            if not dp[i]:
                for prime in primes:
                    if i % prime == 0:
                        dp[i] = True
                        break

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_round(n):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
