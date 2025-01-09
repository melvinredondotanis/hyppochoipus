#!/usr/bin/env python3

from time import sleep
from random import choice

import ollama

from header import welcome, settings
from loaders import get_students_from_json, get_message_by_type
from voice import TextToSpeech
from stt import speech_to_text


MODEL = 'hyppochoipus'
MESSAGES_FILE = 'config/locales.json'


def choose_house():
    houses = ['Segfaultdor', 'Algodaigle', 'Stackouffle', 'Pythontard']
    return choice(houses)


def say(message):
    try:
        VOICE.say(message['response'])
        print(message['response'])
    except NameError:
        print(message['response'])


def generate_message(model, message):
    try:
        return ollama.generate(model, message)
    except Exception as e:
        print(f'Error: {e.error}')
        exit(1)


def verify_model(model):
    try:
        ollama.show(model)
    except ollama.ResponseError as e:
        print('Error:', e.error)
        exit(1)


def main():
    welcome()
    verify_model(MODEL)

    whisper_model, language, tts_status = settings()
    stt_status = True

    if tts_status:
        global VOICE
        VOICE = TextToSpeech(language=language)

    students = get_students_from_json('config/students.json')
    message = get_message_by_type(MESSAGES_FILE, language, 'welcome')

    response = generate_message(MODEL, message)
    say(response)

    for student in students:
        print(f'\n[{student}]')
        sleep(5)

        student_responses = {}

        for i in range(4):
            message = get_message_by_type(MESSAGES_FILE, language, 'question_{}'.format(i+1))
            response = generate_message(MODEL, message)

            if tts_status:
                say(response)
            else:
                print(response['response'])

            sleep(1)

            if stt_status:
                answer = speech_to_text(whisper_model, language)
                print(f'[{student}]: {answer}')
            else:
                answer = input('Answer: ')
                print(f'[{student}]: {answer}')

            student_responses[f'question_{i+1}'] = {
            'question': response['response'],
            'answer': answer
            }

        house = choose_house(student_responses)
        message = get_message_by_type(MESSAGES_FILE, language, 'house')
        message = message.replace('{student_name}', student)
        message = message.replace('{house}', house)
        response = generate_message(MODEL, message)
        say(response)
        say({'response': get_message_by_type(MESSAGES_FILE, language, 'next')})

    message = get_message_by_type(MESSAGES_FILE, language, 'end')
    response = generate_message(MODEL, message)
    say(response)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('Program terminated by user.')
    finally:
        print('Cleaning up.')
