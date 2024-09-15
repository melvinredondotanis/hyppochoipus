#!/usr/bin/env python3

from os import remove
from header import welcome, settings
from speech_to_text import speech_to_text
from ollama import chat

def main():
    model, language, students = settings()
    messages = []
    while students > 0:
        user_input = speech_to_text(model, language)
        if not user_input:
            exit()
        print()
        messages.append({"role": "user", "content": user_input})
        message = chat(messages)
        messages.append(message)
        print("\n\n")
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
