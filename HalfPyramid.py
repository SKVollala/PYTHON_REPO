"""
This program prints a half pyramid.

Input:
It asks you to enter a number.

Output:
Prints a half number pyramid until the number you entered.
"""


def half_pyramid():
    num = input("Enter a number: ")
    for i in range(1, int(num) + 1):
        for j in range(1, i+1):
            print(j, end=" ")
        print("\n", end="")


if __name__ == "__main__":
    half_pyramid()
