#!/usr/bin/env python3

from os import remove

from faster_whisper import WhisperModel

from header import welcome
from speech_to_text import speech_to_text
from ollama import *

def main():
    messages = []
    while True:
        user_input = speech_to_text("tiny", "fr")
        if not user_input:
            exit()
        print()
        messages.append({"role": "user", "content": user_input})
        message = chat(messages)
        messages.append(message)
        print("\n\n")

if __name__ == "__main__":
    try:
        welcome()
        main()
    except KeyboardInterrupt or EOFError:
        print("\nProgram terminated by user")
    finally:
        print("Cleaning up...")
        try:
            remove("audio.wav")
        except FileNotFoundError:
            pass
