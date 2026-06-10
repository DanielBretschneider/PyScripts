#! /usr/bin/python3
"""
File:   fuel.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-10

Description:
    In a file called fuel.py, implement a program that prompts the user for a fraction,
    formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer,
    and then outputs, as a percentage rounded to the nearest integer, how much fuel is
    in the tank. If, though, 1% or less remains, output E instead to indicate that the
    tank is essentially empty. And if 99% or more remains, output F instead to indicate
    that the tank is essentially full.

Info:
    https://cs50.harvard.edu/python/psets/3/fuel/

"""


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # user input
    fraction = input("Fraction: ")

    # process input
    process_fraction(fraction)


def process_fraction(frac):
    """
    Check input, calculate and/or throw err
    """
    # check if input is correctly formatted
    if check_input_format(frac):
        # get x and y
        x, y = frac.split("/")

        # convert to int
        int_x, int_y = int(x), int(y)

        # calculate
        percent = calculate_percent(int_x, int_y)

        # if 1% or less -> E
        # if 99% or more -> F
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(str(round(percent)) + "%")

    else:
        # ask again
        fraction = input("Fraction: ")

        # recursive func call
        process_fraction(fraction)


def check_input_format(frac):
    """
    Should be numbers in x/y format
    """
    if "/" in frac:
        # get both x and y
        x, y = frac.split("/")

        # check if both strings are numbers
        if x.isnumeric() and y.isnumeric():
            return True
        else:
            return False

    return False


def calculate_percent(x, y):
    """
    Calculate percentage of fuel gauge
    """
    # if X is greater than Y, or Y is 0, instead prompt the user again
    if x > y or y == 0:
         # ask again
        fraction = input("Fraction: ")

        # func call
        process_fraction(fraction)
    else:
        # calculate percent
        percent = float((x / y) * 100)

        # round up
        percent = round(percent)

        # return result
        return percent


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
