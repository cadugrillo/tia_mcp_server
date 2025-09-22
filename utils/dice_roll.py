import random

def roll_two_dice() -> int:
    """
    Simulate rolling two six-sided dice and return their values combined.
    Returns:
        int: The sum of the two dice rolls.
    """
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2
