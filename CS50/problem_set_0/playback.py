#! /usr/bin/python3
"""
File:   playback.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-07

Description:
    In a file called playback.py, implement a program in Python that prompts
    the user for input and then outputs that same input, replacing each
    space with ... (i.e., three periods).

Info:
    https://cs50.harvard.edu/python/psets/0/playback/

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

    # replace space with '...'
    user_input_replaced = user_input.replace(" ", "...")

    # print user_input
    print("[*] Output: " + user_input_replaced)


# This condition checks if the script is being run directly
# (as opposed to being imported as a module in another script).
if __name__ == "__main__":
    # Call the main function to start the program
    main()
