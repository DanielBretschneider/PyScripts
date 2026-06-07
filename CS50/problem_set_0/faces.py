#! /usr/bin/python3
"""
File:   playback.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-07

Description:
    In a file called faces.py, implement a function called convert that accepts a
    str as input and returns that same input with any :) converted to 🙂 (otherwise
    known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a
    slightly frowning face). All other text should be returned unchanged.

Info:
    https://cs50.harvard.edu/python/psets/0/faces/

"""


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # read user input
    user_input = input("[*] Enter your message: ")

    # replace simlies
    user_input_replaced = user_input.replace(":)", "🙂")
    user_input_replaced = user_input_replaced.replace(":(", "🙁")

    # print user_input
    print(user_input_replaced)


# This condition checks if the script is being run directly
# (as opposed to being imported as a module in another script).
if __name__ == "__main__":
    # Call the main function to start the program
    main()
