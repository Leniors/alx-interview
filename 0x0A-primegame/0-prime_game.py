#!/usr/bin/python3
"""
Prime Game Module: Defines function that determines the winner after a certain
number of rounds of playing the Prime Game.
"""


def isWinner(x, nums):
    """isWinner

    Determine who is the winner after a certain number of rounds.

    Argumnets:
        x (int): The number of rounds
        nums (List[int]): List of all the n's for each round.

    Return:
        (str): The name of the player who wins.
    """
    if x < 1 or not nums:
        return None

    # Helper function to determine prime numbers up to the max n
    def sieve_of_eratosthenes(max_n):
        is_prime = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if is_prime[p]:
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, max_n + 1) if is_prime[p]]
        return prime_numbers

    # Get all primes up to the largest number in nums
    max_num = max(nums)
    prime_numbers = sieve_of_eratosthenes(max_num)
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = [p for p in prime_numbers if p <= n]
        turn = 0  # 0 for Maria, 1 for Ben
        
        while primes_in_game:
            prime = primes_in_game[0]
            primes_in_game = [p for p in primes_in_game if p % prime != 0]

            turn = 1 - turn
        
        if turn == 1:  # If turn is 1, it means Ben made the last valid move and Maria cannot move
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
