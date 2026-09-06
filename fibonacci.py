#!/usr/bin/env python3
"""
A simple script to print the Fibonacci sequence.
"""


def print_fibonacci(n: int) -> None:
    """
    Print the first n numbers in the Fibonacci sequence.
    
    Args:
        n: The number of Fibonacci numbers to print.
    """
    if n <= 0:
        print("Please enter a positive number.")
        return
    
    # Initialize first two Fibonacci numbers
    a, b = 0, 1
    
    print(f"Fibonacci sequence (first {n} numbers):")
    
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    
    print()  # Print newline at the end


if __name__ == "__main__":
    # Print the first 10 Fibonacci numbers
    print_fibonacci(10)
    
    # Uncomment below to print a custom amount
    # count = int(input("How many Fibonacci numbers would you like to see? "))
    # print_fibonacci(count)
