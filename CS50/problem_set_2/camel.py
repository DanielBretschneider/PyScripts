#! /usr/bin/python3
"""
File:   camel.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-08

Description:
    In a file called camel.py, implement a program that prompts the user for the name of a
    variable in camel case and outputs the corresponding name in snake case. Assume that
    the user’s input will indeed be in camel case.

Info:
    https://cs50.harvard.edu/python/psets/2/camel/

"""


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # get expression from user
    user_input = input("camelCase: ")

    # convert to snake case
    conv_str = convert_to_snake_case(user_input)

    # print converted string
    print("snake_case: " + conv_str)


def convert_to_snake_case(input):
    """
    converts camel case names to snake case
    f.e.: userNameField -> user_name_field

    :return: String
    """
    # var for new str
    new_str = ""

    # loop through given str (input)
    for c in range(len(input)):
        # current char
        curr_char = input[c]

        # check if char is upper case
        if curr_char.isupper():
            new_str = new_str + "_" + curr_char.lower()
        else:
            new_str += curr_char

    # return converted snake case string
    return new_str


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
