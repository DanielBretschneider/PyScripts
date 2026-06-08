#! /usr/bin/python3
"""
File:   bank.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-08

Description:
    In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”,
    output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading
    whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

    Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
    Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

Info:
    https://cs50.harvard.edu/python/psets/1/bank/

"""

#
# Globals
#
# we don't need no 'hello'
bad_word = "hello"

# that's what you get for helloing
hello_msg = "$0\n"

# starting with 'h' is not a good idea
h_start_msg = "$20\n"

# successfull greetings
success_msg = "$100\n"


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # read in greeting
    user_greeting = input("Greeting: ")

    # do the magic
    process_greeting(user_greeting)


def process_greeting(greeting):
    """
    Implement logic needed for the exercise

    :return: None
    """
    # prepare greeting - for safety reasons
    greeting = greeting.lower()
    greeting = greeting.strip()

    # check if greeting contains hello
    if greeting.startswith(bad_word):
        # you said it
        print(hello_msg)
    elif greeting.startswith("h"):
        # better
        print(h_start_msg)
    else:
        # best
        print(success_msg)


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
