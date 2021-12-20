'''
Vacation Destination Random Generator
Sharon Steinke
December 19, 2021

A simple random generator specifically for choosing vacation destinations.
To use: type name of destination, press enter, type name of destination, etc...
and type 'done' to recieve randomly selected destination.
'''
import random

def get_vacay_lyst(vacay_file):
    '''reads a file and stores destinations in a list'''
    with open(vacay_file, "r") as vacays:
        vacay_lyst = []
        for line in vacays:
            lyst = line.strip().split('\n')
            vacay_lyst.append(lyst[0])
        return vacay_lyst


def vacay_generator(vacay_file):
    '''takes destination inputs and stores into list. 
    Then picks a random destination and prints'''
    vacays = get_vacay_lyst(vacay_file)
    print('Welcome to Vacation Destination Generator')
    start_stop = ''
    while start_stop.upper() != 'N':
        start_stop = input('Generate new destination? (Y/N): ')
        if start_stop.upper() == 'Y':
            new_destination = random.choice(vacays)
            final_vacation_destination = print(f'Pack your bags, you are going to: {new_destination}')
            return final_vacation_destination
    
def main():
    vacay_generator('vacay_dest.txt')


if __name__ == "__main__":
    
    main()
