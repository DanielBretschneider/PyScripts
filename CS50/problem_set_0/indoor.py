#! /usr/bin/python3
"""
File:   indoor.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-07

Description:
    In a file called indoor.py, implement a program in Python that prompts 
    the user for input and then outputs that same input in lowercase. Punctuation 
    and whitespace should be outputted unchanged. You’re welcome, but not required, 
    to prompt the user explicitly, as by passing a str of your own as an argument 
    to input.

Info:
    https://cs50.harvard.edu/python/psets/0/indoor/

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
    
    # to lowercase
    user_input_lowercase = user_input.lower()

    # print user_input
    print("[*] Output: " + user_input_lowercase)
    

# This condition checks if the script is being run directly
# (as opposed to being imported as a module in another script).
if __name__ == "__main__":
    # Call the main function to start the program
    main()