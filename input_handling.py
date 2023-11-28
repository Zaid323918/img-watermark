import os
import cv2

def get_input() -> int:
    choice = ''
    while choice not in ['1', '2']:
        print('Options:')
        print('1. Place a new watermark on an image')
        print('2. Remove a watermark from an image')
        
        choice = input('Input a number: ')

        if choice not in ['1', '2']:
            print(f'\nSorry, {choice} is not a valid option.\n')

    return int(choice)

def get_filename(type_of_file: str) -> str:
    filename = ''
    while filename == '':
        filename = input(f'Please enter full path to {type_of_file} file: ')
        if not os.path.exists(filename):
            print(f'\nSorry, {filename} is not a valid path.\n')
            filename = ''
            continue

        # Check to make sure the file is a valid image
        img = cv2.imread(filename)
        if img is None:
            print(f'\nSorry, {filename} does not contain a valid image.\n')
            filename = ''
            continue

    return filename
