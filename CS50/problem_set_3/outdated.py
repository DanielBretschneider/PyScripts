#! /usr/bin/python3
"""
File:   outdated.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-10

Description:
    In a file called outdated.py, implement a program that prompts
    the user for a date, anno Domini, in month-day-year order, formatted
    like 9/8/1636 or September 8, 1636, wherein the month in the latter
    might be any of the values in the list below:

Info:
    https://cs50.harvard.edu/python/psets/3/outdated/

"""


#
# Functions
#
def main():
    """
    Entry point of the program.
    """

    # user input
    input_date = input("Date: ")

    # process input
    format_date_ISO8601(fraction)


def format_date_ISO8601(u_date):
    """
    Format from MM-DD-YYYY into YYYY-MM-DD or
    format from Month DD, YYYY to YYYY-MM-DD
    """

# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
