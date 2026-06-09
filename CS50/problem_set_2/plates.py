#! /usr/bin/python3
"""
File:   plates.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-09

Description:
    In plates.py, implement a program that prompts the user for a vanity plate
    and then output Valid if meets all of the requirements or Invalid if it does
    not.

    Requirements for valid vanity plate:
    - Start with at least two letters
    - Max. 6 characters (letters or numbers) and a min. of 2 characters
    - No Numbers in the middle of the plate -> only at the end f.e. AAA222
    - First Number cannot be 0
    - No periods, spaces, punctuation marks etc.

Info:
    https://cs50.harvard.edu/python/psets/2/plates/

"""

#
# Globals
#
MAX_LENGTH = 6
MIN_LENGTH = 2


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # get plate
    plate = input("Plate: ")

    # is_valid checks if plate is valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    """
    valid if all requirements are met
    """
    # length of plate
    len_plate = len(plate)

    # long if statement
    if (
        plate.isalnum() and                     # no special characters
        is_valid_length(len_plate) and          # check if length is valid
        starts_with_letters(plate) and          # check if starts with at least two letters
        not has_numbers_inbetween(plate) and    # check if numbers only occur at the end
        not check_first_number_is_zero(plate)       # check if first number is zero
    ):
        return True
    else:
        return False


def is_valid_length(length):
    """
    returns True if length of plate is valid
    """
    if MIN_LENGTH <= length <= MAX_LENGTH:
        return True
    else:
        return False


def starts_with_letters(plate):
    """
    returns True if first two characters of plate are letters
    """
    return plate[:2].isalpha()


def has_numbers_inbetween(plate):
    """
    returns True if numbers in between letters were found
    """
    # no letter after first number
    found_letter_after_number = False

    # number found
    number_found = False

    for c in range(len(plate)):
        if plate[c].isnumeric():
            number_found = True
        else:
            if number_found == True and plate[c].isalpha():
                found_letter_after_number = True

    # return
    return found_letter_after_number


def check_first_number_is_zero(plate):
    """
    returns True if first found number of plate is a 0
    """
    for c in range(len(plate)):
        if plate[c].isnumeric():
            return int(plate[c]) == 0


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()

