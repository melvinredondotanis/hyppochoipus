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


def settings():
    """
    This function displays the settings menu
    and waits for the user to select a model, language, and number of students.

    Returns:
        tuple: The selected model, language, and number of students
    """

    models = [
        "tiny",
        "small",
        "medium",
        "large",
        "huge"
    ]

    languages = [
        "en",
        "fr"
    ]

    for i, model in enumerate(models, start=0):
        print("[{}] {}".format(i, model))

    try:
        model_number = int(input("Select a model [number]: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for i, language in enumerate(languages, start=0):
        print("[{}] {}".format(i, language))

    try:
        language_number = int(input("Select a language [number]: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    try:
        students_number = int(input(
                                    "Select the number of students [number]: "
                                    ))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    system("clear")
    return models[model_number], languages[language_number], students_number


if __name__ == "__main__":
    welcome()
    settings()
