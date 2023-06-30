#!/usr/bin/python3
"""Prime Game.
"""


def isWinner(x, numbers):
    """Determines the winner of a prime game session with `x` rounds.
    """
    players = ('Maria', 'Ben')
    winners = []
    nums_length = len(numbers) if numbers else 0
    if nums_length == 0:
        return None
    for i in range(x):
        n = numbers[i] if i < nums_length else 0
        n_nums = list(range(1, n + 1, 1))
        prime = 2
        turns = 0
        while True:
            remove_ocurred = False
            p_multiples = list(range(prime, n + 1, prime))
            for p_multiple in p_multiples:
                if p_multiple in n_nums:
                    n_nums.remove(p_multiple)
                    remove_ocurred = True
            turns += 1
            if remove_ocurred:
                for val in n_nums:
                    if val > prime:
                        prime = val
                        break
            else:
                break
        winners.append(players[turns % 2])
    marias_wins = winners.count(players[0])
    bens_wins = winners.count(players[1])
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
