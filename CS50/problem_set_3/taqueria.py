#! /usr/bin/python3
"""
File:   taqueria.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-10

Description:
    In a file called taqueria.py, implement a program that enables a user to place an order,
    prompting them for items, one per line, until the user inputs control-d (which is a common
    way of ending one’s input to a program). After each inputted item, display the total cost
    of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal
    places. Treat the user’s input case insensitively. Ignore any input that isn’t an item.
    Assume that every item on the menu will be titlecased.

Info:
    https://cs50.harvard.edu/python/psets/3/taqueria/

"""

#
# Gloabls
#
ENTREES = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # total price
    total = 0

    # user input
    while(True):
        try:
            # get item
            curr_item = input("Item: ").capitalize()

            # prepare input (upper / lower)
            if " " in curr_item:
                substr_1, substr_2 = curr_item.split(" ")
                curr_item = substr_1 + " " + substr_2.capitalize()

            # check order
            order = check_order(curr_item)

            # check return val and print subtotal
            if order > 0:
                total += order
                print("Total: " + format_price(total))

        except EOFError:
            # catch crtl+d input and print total
            print("\nTotal: " + format_price(total))

            # end
            return


def check_order(item):
    """
    Check if items exists and return it's price or
    0 if the item does not exist
    """
    if item in ENTREES:
        return float(ENTREES[item])
    else:
        return 0


def format_price(price):
    """
    Format float number as $xx.yy
    """
    # round to two decimals
    price = round(price, 3)

    # add dollar sign and leave trailing zero of float number
    str_price = "$" + "%.2f" % price

    # return string with dollar sign
    return str_price


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
