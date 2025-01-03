#!/usr/bin/env python3

import ollama
from header import welcome, settings
from loaders import get_students_from_json, get_message_by_type


MODEL = 'hyppochoipus'
MESSAGES_FILE = 'messages.json'


# lancer un message de bienvenue generate: donner la liste et la description des maison, présenter leurs représentent
# puis faire un chat pour chaque étudiant chat::
# poser quelques questions
# annoncer la maison
# faire une annonce de fin: le nombre de chat / étudiant est ok alors generate -> message
# il passe au suivant avec un json et le nom des éléves
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

    whisper_model, language, students_number = settings()

    students = get_students_from_json('students.json')
    message = get_message_by_type(MESSAGES_FILE, language, 'welcome')

    response = generate_message(MODEL, message)
    print(response['response'])


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('Program terminated by user.')
    finally:
        print('Cleaning up.')
        
