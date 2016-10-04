# -*- coding: utf-8 -*-

def convert_file():
    with open('numbers.txt', 'r') as fd:
        file_data = fd.read()
    list_numbers = file_data.replace('\n', '').split(',')
    for number in list_numbers:
        print(number)

if __name__ == '__main__':
    convert_file()
