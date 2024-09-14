#!/usr/bin/env python3

from os import system


def welcome():
    """
    This function displays a welcome message
    and waits for the user to press Enter to start.
    """

    system("clear")
    print("\nHyppochoipus")
    print("By Melvin Redondo--Tanis\n")
    print("Contibutors:")
    print("    - Remi Marçais")
    print("")
    print("To exit press Ctrl+C")
    input("Press Enter to start...")
    system("clear")
