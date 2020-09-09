"""
SBB Task 4a - Student Record

Rachael Graveling
09/09/2020

A brief description of what the program does
"""

class Record():
    def __init__(self, name, age, height, town):
        self.name = name
        self.age = age
        self.height = height
        self.town = town

def main():
    student = get_record()
    display_record(student)

def get_record():
    name = input('Please enter name: ')
    age = int(input('Please enter age: '))
    while age < 1 or age > 150 or not age.is_integer():
        print('Error. Must be a whole number between 1 & 150')
        age = float(input('Please enter age : '))

    height = float(input('Please enter height: '))
    while height < 1 or height > 2.5:
        print('Error. Must be a number between 1 & 2.5')
        height = float(input('Please enter height : '))
    town = input('What is your home town?: ')

    return Record(name, age, height, town)

def display_record(record):
    print()
    print(record.name, record.age, record.height, record.town)

main()

