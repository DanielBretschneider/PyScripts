#! /usr/bin/python3
"""
File:   coke.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-08

Description:
    In a file called coke.py, implement a program that prompts the user to insert a coin,
    one at a time, each time informing the user of the amount due. Once the user has
    inputted at least 50 cents, output how many cents in change the user is owed. Assume that
    the user will only input integers, and ignore any integer that isn’t an accepted denomination.

Info:
    https://cs50.harvard.edu/python/psets/2/coke/

"""

#
# Globals
#

# global counter
INPUTTED_COINS = 0

# price for a coke
PRICE = 50

# accepted coins
accept_coins = [5, 10, 25]


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    global INPUTTED_COINS

    # check if coke is payed up
    while INPUTTED_COINS < 50:
        # amount due
        amount_due = PRICE - INPUTTED_COINS

        # print amount to pay / left
        print("Amount Due: " + str(amount_due))

        # amount input
        user_input = input("Insert coin: ")

        # check if enough
        check_inputted_coins(int(user_input))


def check_inputted_coins(coin):
    """
    Only 5, 10 and 25 cents are accepted.
    If you throw any other coins into the machine,
    you won't get them back - only change.
    """
    global INPUTTED_COINS

    # loop through coins and check
    for c in accept_coins:
        if coin == c:
            INPUTTED_COINS += coin

    # check if max reached
    if INPUTTED_COINS >= 50:
        change = INPUTTED_COINS - PRICE
        print("Change Owed: " + str(change))


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
