#!/usr/bin/env python3

from os import system


def welcome():
    system('clear')
    print('\nHyppochoipus\n')
    print('To exit press Ctrl+C')
    input('Press Enter to start...')
    system('clear')


def display_options(options):
    for i, option in enumerate(options):
        print(f'[{i}] {option}')


def get_selection(prompt, options):
    while True:
        try:
            selection = int(input(prompt))
            if 0 <= selection < len(options):
                return selection
            else:
                print('Invalid number. Please enter a valid number.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')


def settings():
    models = [
        'tiny.en', 'tiny', 'base.en',
        'base', 'small.en', 'small',
        'medium.en', 'medium', 'large-v1',
        'large-v2', 'large-v3', 'large',
        'distil-large-v2', 'distil-medium.en', 'distil-small.en',
        'distil-large-v3'
    ]
    languages = ['en', 'fr']

    display_options(models)
    model_number = get_selection('Select a model [number]: ', models)

    display_options(languages)
    language_number = get_selection('Select a language [number]: ', languages)

    system('clear')
    return models[model_number], languages[language_number]
