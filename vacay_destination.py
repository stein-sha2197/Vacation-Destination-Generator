'''
Vacation Destination Random Generator
Sharon Steinke
December 19, 2021

A simple random generator specifically for choosing vacation destinations.
To use: enter destinations, one per line, in plain txt document. Make sure there are no 
new lines at the end of the list. call vacay_generator with location of your file as
a parameter. 
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
    '''picks a random destination from list'''
    vacays = get_vacay_lyst(vacay_file)
    print('Welcome to Vacation Destination Generator')
    start_stop = ''
    while start_stop.upper() != 'N':
        start_stop = input('Generate  a new destination? (Y/N): ')
        if start_stop.upper() == 'Y':
            new_destination = random.choice(vacays)
            print(f'Pack your bags, you are going to: {new_destination}')
            start_over = input('Would you like to play again? (Y/N): ')
            if start_over.upper() == 'Y':
                return vacay_generator(vacay_file)   
            if start_over.upper() == 'N':
                good_bye  = print(f'Goodbye.')
                return good_bye
        if start_stop.upper() == 'N':
            good_bye  = print(f'Goodbye.')
            return good_bye
    
def main():
    vacay_generator('vacay_dest.txt')


if __name__ == "__main__":
    
    main()
