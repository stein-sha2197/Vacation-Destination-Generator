"""
Vacation Destination Random Generator
Sharon Steinke
December 19, 2021

A simple random generator specifically for choosing vacation destinations.
To use: enter destinations, one per line, in plain txt document. Call vacay_generator with location of your file as
a parameter. 
"""
import random

def get_vacay_lyst(vacay_file):
    """reads a file and stores destinations in a list"""
    with open(vacay_file, "r") as vacays:
        vacay_lyst = []
        for line in vacays:
          vacay_lyst.append(line)
        return vacay_lyst
        
def vacay_generator(vacay_file):
    """picks a random destination from list"""
    vacays = get_vacay_lyst(vacay_file)
    print("Welcome to Vacation Destination Generator\n")
    start_stop = input("Generate  a new destination? (Y/Q): ")
    while start_stop.upper() != 'Q':
        new_destination = random.choice(vacays)
        print(f"\nPack your bags, you are going to: {new_destination}")
        start_stop = input("Generate a new destination? (Y/Q): ")
          
    good_bye  = print("\nGoodbye.")
    return good_bye
    
def main():
    vacay_generator('vacay_dest.txt')

if __name__ == "__main__":
    
    main()
