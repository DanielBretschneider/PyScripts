#! /usr/bin/python3
"""
File:   extensions.py
Author: Daniel Bretschneider, daniel@bretschneider.cc
Date:   2026-06-08

Description:
    In a file called extensions.py, implement a program that prompts the user for the name of a file
    and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

Info:
    https://cs50.harvard.edu/python/psets/1/extensions/

"""

#
# Globals
#
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types
file_extensions = {
    "gif" : "image/gif",
    "jpg" : "image/jpeg",
    "jpeg": "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "txt" : "text/plain",
    "zip" : "application/zip"
}

# unknown or missing suffix
suffix_err = "application/octet-stream"


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # read in greeting
    file_name = input("File name: ")

    # prepare to process str
    file_name = file_name.lower()
    file_name = file_name.strip()

    # do the magic
    common_type = process_file_name(file_name)

    # print it!
    print(common_type)


def process_file_name(fname):
    """
    Simple check if given input is a valid filename (name.ext)
    or is missing a suffix

    :return: Suffix as str
    """
    # check if empty
    if len(fname) == 0:
        # return err
        return suffix_err

    # check format (name.ext)
    fname_splitted = fname.split(".")

    # get sum of elements in array
    fname_splitted_length = len(fname_splitted)

    # just a word / invalid file name
    if fname_splitted_length == 1:
        # return err -> no filename
        return suffix_err

    # "normal" case
    elif fname_splitted_length == 2:
        if fname_splitted[1] in file_extensions:
            #return correct common type
            return file_extensions[fname_splitted[1]]
        else:
            # return err -> no filename
            return suffix_err

    # for cases with more than one file extension
    elif fname_splitted_length > 2:
        if fname_splitted[fname_splitted_length-1] in file_extensions:
            #return correct common type
            return file_extensions[fname_splitted[fname_splitted_length-1]]
        else:
            # return err -> no filename
            return suffix_err

    # everything else
    else:
        # return err -> no filename
        return suffix_err


# Run main method
if __name__ == "__main__":
    # Call the main function to start the program
    main()
