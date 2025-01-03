#!/usr/bin/env python3

import json
from sys import exit


def get_students_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data.get('students', [])
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)


def get_message_by_type(file_path, language, message_type):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data.get(message_type, {}).get(language, "")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)
