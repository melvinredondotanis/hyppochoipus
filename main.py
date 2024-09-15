#!/usr/bin/env python3

from os import remove
from header import welcome, settings
from speech_to_text import speech_to_text
from ollama import chat

say_hello = {
    "en": "Welcomes all students for the ceremony.",
    "fr": "Souhaite la bienvenue pour la cérémonie."
    }


def main():
    try:
        model, language, students = settings()
    except TypeError:
        return

    messages = []
    messages.append({"role": "asssistant", "content": say_hello[language]})
    message = chat(messages)
    messages.append(message)
    print("\nHYPPCHOIPUS: {}".format(message["content"]))
    while students > 0:
        user_input = speech_to_text(model, language)
        if not user_input:
            exit()

        print()
        messages.append({"role": "user", "content": user_input})
        message = chat(messages)
        print("\nHYPPCHOIPUS: {}".format(message["content"]))
        messages.append(message)
        students -= 1


if __name__ == "__main__":
    try:
        welcome()
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram terminated by user")
    finally:
        print("Cleaning up...")
        try:
            remove("audio.wav")
        except FileNotFoundError:
            pass
