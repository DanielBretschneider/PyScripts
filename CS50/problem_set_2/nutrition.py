#! /usr/bin/python3
"""
File:   nutrition.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-09

Description:
    In a file called nutrition.py, implement a program that prompts consumers
    users to input a fruit (case-insensitively) and then outputs the number of
    calories in one portion of that fruit, per the FDA’s poster for fruits, which
    is also available as text. Capitalization aside, assume that users will input
    fruits exactly as written in the poster (e.g., strawberries, not strawberry).
    Ignore any input that isn’t a fruit.

Info:
    https://cs50.harvard.edu/python/psets/2/nutrition/

"""

#
# Globals
#
FRUITS = {
    "apple" :           130,
    "avocado" :         50,
    "banana" :          110,
    "cantaloupe" :      50,
    "grapefruit" :      60,
    "grapes" :          90,
    "honeydew Melon" :  50,
    "kiwifruit" :       90,
    "lemon" :           15,
    "lime" :            20,
    "nectarine" :       60,
    "orange" :          80,
    "peach" :           60,
    "pear" :            100,
    "pineapple" :       50,
    "plums" :           70,
    "strawberries" :    50,
    "sweet cherries" :  100,
    "tangerine" :       50,
    "watermelon" :      80,
}


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # get plate
    item = input("Item: ").lower()

    # get calories from dictionary
    if item in FRUITS:
        print("Calories: " + str(FRUITS.get(item)))


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
