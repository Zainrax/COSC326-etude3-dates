import validate_date as vd
import os
import sys
"""
Main program to get input from a user to validate dates.
It can read a file called "dates.txt", or users can manually
input a date to check that it follows the prescribed date format.

Author: Patrick Baxter(baxpa469)
date:8/01/2019
"""

def main():
    """Gets user input for dates to be validated.

    Checks if a user wants to read a file, or manually input the dates
    and runs the validate function from the validate_date module.
    """
    print('This program takes dates from a file, or user input, and validates that it fits the format:\n[d/dd]/[0m/m/mm/first 3 characters of month]/[yy/yyy] seperated by /,-, or <space>.\n')
    op = input('Would you like to read(r) dates file or manually(m) input a date? [r|m|exit]\n')
    while(True):
        if(op == 'exit'): break
        elif(op == 'm'):
            print('Enter date(type "exit" to escape):')
            while(True):
                date = input()
                if(date == 'exit'): break
                print(vd.validate(date))
            break
        elif(op == 'r'):
            filename = input('What is the name of the file including extension(.txt recommended)? eg. "dates.txt"\n')
            while not (os.path.isfile(filename)):
                filename = input('Invalid input, try again:\n')
            with open(filename, 'r') as f:
                for line in f:
                    print(vd.validate(line))
            print('type "exit" to escape:')
            while(True):
                if(input()=='exit'): break
            break
        else:
            op = input('Invalid input, try again:[r|m|exit]\n')

if __name__ == '__main__':
    if not (os.isatty(sys.stdin.fileno())):
        for line in sys.stdin:
            print(vd.validate(line))
    else:
        main()
