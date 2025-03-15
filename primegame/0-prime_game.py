#!/usr/bin/python3
"""
Module that determines which from Ben or Maria
is the strongest at prime game bingo
Given the set of consecutive integers `n` in the set `nums`
Maria & Ben take in turns (Maria always going first) a primer number from
the set, remove that number and its multiple from the set
The player that cannot make a move loses the game
"""


def isWinner(x, nums):
    """
    x -> number of rounds
    nums -> array of n (n maybe different for each rounds)
    """
    # Carrie tricked us
    if x != len(nums):
        return None

    nums.sort()
    primes = greek_fiesta(nums[-1])
    if primes is None:
        return None
    maria = 0
    ben = 0
    for n in nums:
        prime_count = 0
        for prime in primes:
            if (prime <= n):
                prime_count += 1
            else:
                break
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1
    return ("Maria" if maria > ben else "Ben")


def greek_fiesta(num):
    primes = [True for _ in range(num + 1)]
    p = 2
    while (p <= pow(num, 0.5)):
        if primes[p] is True:
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1

    primes = [p for p in range(2, num + 1) if primes[p]]
    return primes
