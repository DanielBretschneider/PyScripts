#! /usr/bin/python3
"""
File:   einstein.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-07

Description:
    In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer
    (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will
    input an integer.

Info:
    https://cs50.harvard.edu/python/psets/0/einstein/

"""

#
# Globals
#
c = 300000000 # speed of light in meters per second m/s


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # read user input
    user_input = input("[*] Enter m in kg : ")

    # convert to int
    m_int = int(user_input)

    # calculate E which is m * c^2
    c_square = c ** 2
    e = m_int * c_square

    # print user_input
    print(e)


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
