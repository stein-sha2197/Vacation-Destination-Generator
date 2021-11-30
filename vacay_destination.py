'''
Vacation Destination Random Generator
Sharon Steinke
November 28, 2021

A simple random generator specifically for choosing vacation destinations. 
To use: type name of destination, press enter, type name of destination, etc...
and type 'done' to recieve randomly selected destination. 
'''
import random

def vacay_generator():
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
    vacay_generator()


if __name__ == "__main__":
    
    main()