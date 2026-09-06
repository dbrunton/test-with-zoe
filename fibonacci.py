#!/usr/bin/env python3

"""Simple Fibonacci sequence generator with clearer names and comments."""

def fibonacci_sequence(count):
    """Yield `count` numbers from the Fibonacci sequence, starting at 0.

    Args:
        count (int): How many Fibonacci numbers to generate.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    first, second = 0, 1  # the two most recent Fibonacci numbers
    while count:
        # yield the current smallest (next) number in the sequence
        yield first
        # advance the pair: new first is the previous second, new second is their sum
        first, second = second, first + second
        count -= 1


if __name__ == "__main__":
    # Print the first 10 Fibonacci numbers separated by spaces
    print(" ".join(map(str, fibonacci_sequence(10))))
