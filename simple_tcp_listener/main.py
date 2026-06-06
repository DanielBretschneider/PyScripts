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


#
# Imports
#
import socket


#
# Globals
#
TCP_IP = "127.0.0.1"
TCP_PORT = 6996
BUFFER_SIZE = 100


#
# Functions
#
def main():
    """
    Entry point of the program.
    """
    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    # connect
    conn, addr = s.accept()
    print("[*] Connection address: ", addr)

    # print out info from connection
    while True:
        data = conn.recv(BUFFER_SIZE)

        if not data:
            break

        print("[*] Received data: ", data)
        conn.send(data)

    # close connection
    conn.close()

# This condition checks if the script is being run directly
# (as opposed to being imported as a module in another script).
if __name__ == "__main__":
    # Call the main function to start the program
    main()