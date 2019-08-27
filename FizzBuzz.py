"""
Author: Santosh Vollala

This program prints iterates the numbers 1 to 100 and prints "Fizz" if the number is a multiple of 3
and "Buzz" if the number is multiple of 5.

Input:
NA

Output:
Prints numbers 1 to 100. If the number is multiple of 3, it prints "Fizz" and
if the number is multiple 5, it prints "Buzz" instead of numbers.
"""


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizz_buzz()
