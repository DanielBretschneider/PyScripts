#! /usr/bin/python3
"""
File:   twttr.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-08

Description:
    In a file called twttr.py, implement a program that prompts the user for a
    str of text and then outputs that same text but with all vowels (A, E, I, O, and U)
    omitted, whether inputted in uppercase or lowercase.

Info:
    https://cs50.harvard.edu/python/psets/2/twttr/

"""

#
# Globals
#

# vowels
VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # get user input
    user_input = input("Input: ")

    # output
    output = ""

    # loop through
    for c in range(len(user_input)):
        # current char
        curr_char = user_input[c]

        # check if vowel
        if not curr_char in VOWELS:
            output += curr_char

    # print output
    print("Output: "+ output)


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
