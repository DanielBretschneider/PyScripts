#! /usr/bin/python3
"""
File:   meal.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-08

Description:
    In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time,
    lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the
    user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range
    is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

    Structure your program per the below, wherein convert is a function (that can be called by main) that converts
    time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like
    "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

    Keep in mind that there are 60 minutes in 1 hour. <- THANKS!

Info:
    https://cs50.harvard.edu/python/psets/1/meal/

"""


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # get expression from user
    user_input = input("Current Time: ")

    # process time and check time format
    if "a.m." in user_input:
        f_time = convert_12(user_input)
    elif "p.m." in user_input:
        f_time = convert_12(user_input)
    else:
        f_time = convert(user_input)

    # check if it's legal to eat something
    check_if_mealtime(f_time)


def convert(time):
    """
    convert is a function (that can be called by main) that converts
    time, a str in 24-hour format, to the corresponding number of hours
    """
    # split time
    h, m = time.split(":")

    # turn time into corresponding float
    new_m = float(m)/60
    new_h = float(h)
    new_time = round(new_h + new_m, 2)

    # return calculated and rounded time
    return new_time


def convert_12(time):
    """
    convert is a function (that can be called by main) that converts
    time, a str in 24-hour format, to the corresponding number of hours
    """
    # split time
    s_time, ampm = time.split(" ")
    h, m = s_time.split(":")

    # turn time into corresponding float
    new_m = float(m)/60
    new_h = float(h)

    # check if am or pm
    if ampm == "p.m.":
        new_h += 12

    # round
    new_time = round(new_h + new_m, 2)

    # return calculated and rounded time
    return new_time


def check_if_mealtime(f_time):
    """
    breakfast between 7:00 and 8:00
    lunch between 12:00 and 13:00
    dinner between 18:00 and 19:00
    """
    # breakfast
    if is_between(7.0, f_time, 8.0):
        print("breakfast time")
    elif is_between(12.0, f_time, 13.0):
        print("lunch time")
    elif is_between(18.0, f_time, 19.0):
        print("dinner time")
    else:
        return


def is_between(a, x, b):
    """
    check if value is between two other values
    """
    if x == a:
        return True
    elif x == b:
        return True

    return min(a, b) < x < max(a, b)


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()

