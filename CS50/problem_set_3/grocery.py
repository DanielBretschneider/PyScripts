#! /usr/bin/python3
"""
File:   grocery.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-10

Description:
    In a file called grocery.py, implement a program that prompts the
    user for items, one per line, until the user inputs control-d
    (which is a common way of ending one’s input to a program). Then
    output the user’s grocery list in all uppercase, sorted alphabetically
    by item, prefixing each line with the number of times the user inputted
    that item. No need to pluralize the items. Treat the user’s input case-insensitively.

Info:
    https://cs50.harvard.edu/python/psets/3/grocery/

"""

#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # item list
    item_list = []

    # generate grocery list
    while(True):
        # check for crtl+d
        try:
            # read in new item
            new_item = input("")
        except EOFError:
            # display items sorted and their occurence
            finish_groceries(item_list)

            # end
            return

        # add to list
        item_list.append(new_item)


def finish_groceries(items):
    """
    count occurence of each item
    print in alphatical order
    """
    # check if list is empty
    if len(items) == 0:
        return

    # list is not empty
    # count frequency of each item and add to dict
    frequency = {}

    # loop through list
    for item in items:
        frequency[item] = frequency.get(item, 0) + 1

    # sort
    sorted_frequency = dict(sorted(frequency.items()))

    # print it
    print_finished_groceries(sorted_frequency)


def print_finished_groceries(dict):
    """
    Print alphabetically uppercase with frequency
    """
    print("")

    # loop through and print
    for key, value in dict.items():
        print(str(value) + " " + str(key).upper())


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
