#! /usr/bin/python3
"""
File:   deep.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-08

Description:
    In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
    the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two
    or forty two. Otherwise output No.

    No need to convert the user’s input to an int if you check for equality with "42", a str, rather than 42, an int!
    It’s okay if your output or the user’s wraps onto multiple lines.

Info:
    https://cs50.harvard.edu/python/psets/1/deep/

"""


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    # check if user is correct
    is_correct = check_answer(user_input)

    # print 'Yes' or 'No' depending on answer
    if is_correct:
        print("Yes")
    else:
        print("No")



def check_answer(user_inp):
    """
    Check if users answer is correct.

    Correct answer is 42, forty two or forty-two

    :return: True or False
    """
    # list of possible answers
    possible_answers = ["42", "forty two", "forty-two"]

    # prepare answer str for comparison
    user_inp = user_inp.lower() # to lower case
    user_inp = user_inp.strip() # remove leading or trailing spaces

    # loop through all the correct answers and compare
    for current_answer in possible_answers:

        # compore given answer to any element of list
        # if correct print 'Yes' and return
        if user_inp == str(current_answer):

            # return True because right answer was given
            return True

    # after all iterations no match? User has to read the hitchhiker's guide to the Galaxy!!
    return False


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
