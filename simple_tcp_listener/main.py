#! /usr/bin/python3
"""
File:   main.py
Author: Daniel Bretschneider
Date:   2026-06-06

Description:
    This is the main entry point for the simple TCP listener application.
    Currently, it prints a basic greeting message to the console.

Info:
    Packages have to be added using 'uv'
    Example: uv add pysnmp

Modules:
    - pysnmp
    - python-nmap
"""

import socket

def main():
    """
    Entry point of the program.
    """
    s = socket.socket()
    s.connect(("127.0.0.1", 22))

    answer = s.recv(1024)
    print(answer)

    s.close()


# This condition checks if the script is being run directly
# (as opposed to being imported as a module in another script).
if __name__ == "__main__":
    # Call the main function to start the program
    main()