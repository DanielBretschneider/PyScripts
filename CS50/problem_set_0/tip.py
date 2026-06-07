#! /usr/bin/python3
"""
File:   tip.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-07

Description:
    In the United States, it’s customary to leave a tip for your server after dining in a restaurant,
    typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written
    a tip calculator for you, below!

    In Austria we tip very similar... :)

    Implement:
        - dollars_to_float
        - percent_to_float

    Assume that the user will input values in the expected formats.

Info:
    https://cs50.harvard.edu/python/psets/0/tip/

"""


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # invoice amount total
    dollars = dollars_to_float(input("How much was the meal? "))

    # percentage one would like to tip (depending on service oc)
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # calculate tip
    tip = dollars * percent

    # print calculated tip advise
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
        which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
        remove the leading $, and return the amount as a float. For instance, given $50.00 as input,
        it should return 50.0.
    """
    # remove leading dollar sign
    dollars_substr = d[1:]

    # convert to float
    converted_dollars = float(dollars_substr)

    # return input as float
    return converted_dollars


def percent_to_float(p):
    """
        which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove
        the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
    """
    # remove trailing percentage sign
    percentage_substr = "0." + p[:-1]

    # convert from str to float
    converted_percentage = float(percentage_substr)

    # return converted value
    return converted_percentage


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
