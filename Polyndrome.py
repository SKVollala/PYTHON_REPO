"""
Author: Santosh Vollala

This program finds out whether a given string/number is a Palindrome or not.

Input:
It asks you to enter a string.

Output:
Prints "YES" if the given string is a Palindrome and "NO" it it's not.
"""


def reverse_slicing(s):
    return s[::-1]


def palindrome():
    input_str = input("Please enter a string: ")
    trim_space = input_str.replace(" ", "")
    reverse_str = reverse_slicing(trim_space)
    if trim_space == reverse_str:
        print("YES, Entered String is a Palindrome")
    else:
        print("NO, Entered String is NOT a Palindrome")


if __name__ == "__main__":
    palindrome()
