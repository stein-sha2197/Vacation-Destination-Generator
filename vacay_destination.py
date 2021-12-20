'''
Vacation Destination Random Generator
Sharon Steinke
November 28, 2021

A simple random generator specifically for choosing vacation destinations. 
To use: type name of destination, press enter, type name of destination, etc...
and type 'done' to recieve randomly selected destination. 

If I were to change anything or update this code to be more user friendly,
I would have it be able to import a list of destinations and keep track of the 
places it had picked and remove it from the list. This way we could keep the
same list without typing it in everytime. As it is, it does what I need it to do.
'''
import random
import csv

def get_vacay_lyst(vacay_file):
    '''reads a file and stores destinations in a list'''
    with open(vacay_file, "r") as vacays:
        vacay_lyst = []
        for line in vacays:
            lyst = line.strip().split('\n')
            vacay_lyst.append(lyst[0])
        return vacay_lyst


def vacay_generator():
    '''takes destination inputs and stores into list. 
    Then picks a random destination and prints'''
    vacay_dest = []
    new_destination = ''
    print('Welcome to Vacation Destination Generator')
    while new_destination != 'done':
        new_destination = input("Please enter a destination or type 'done': ")
        vacay_dest.append(new_destination)
    vacay_dest.pop()
    final_destination = random.choice(vacay_dest)
    final_vacation_destination = print(f'Pack your bags, you are going to: {final_destination}')
    return final_vacation_destination
    
def main():
    print(get_vacay_lyst("vacay_dest.txt"))


if __name__ == "__main__":
    
    main()
