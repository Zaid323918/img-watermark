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

def get_scale() -> float:
    scale_str = ''
    scale = 0.0
    while scale_str == '':
        scale_str = input('Please enter the desired scale of the watermark compared to the image (0 - 1): ')
        try:
            scale = float(scale_str)
            if scale > 1.0 or scale < 0.0:
                print(f'Sorry, {scale_str} is not in the range (0 - 1).\n')
                scale_str = ''
                continue
        except:
            print(f'\nSorry, {scale_str} is not a number.\n')
            scale_str = ''
            continue

    return scale

def get_transparency() -> float:
    tranparency_str = ''
    transparency = 0.0
    while tranparency_str == '':
        tranparency_str = input('Please enter the desired transparency of the watermark (0 - 1): ')
        try:
            transparency = float(tranparency_str)
            if transparency > 1.0 or transparency < 0.0:
                print(f'Sorry, {tranparency_str} is not in the range (0 - 1).\n')
                tranparency_str = ''
                continue
        except:
            print(f'\nSorry, {tranparency_str} is not a number.\n')
            tranparency_str = ''
            continue

    return transparency
