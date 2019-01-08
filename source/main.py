import validateDate as vd
"""
Main program to get input from a user to validate dates.
It can read a file called "dates.txt", or users can manually
input a date to check that it follows the prescribed date format.

Author: Patrick Baxter(baxpa469)
date:8/01/2019
"""
print('This program takes dates from "dates.txt" or user input and validates that it fits the format:\n[d/dd]/[0m/m/mm/first 3 characters of month]/[yy/yyy]\n')
op = input('Would you like to read(r) dates file or manually(m) input a date? [r|m|exit]\n')
while(True):
    if(op == 'exit'): break
    elif(op == 'm'):
        print('Enter date(type "exit" to escape):')
        while(True):
            date = input()
            if(date == 'exit'): break
            print(vd.validate(date))
    elif(op == 'r'):
        with open("dates.txt", 'r') as f:
            for line in f:
                print(vd.validate(line))
        print('type "exit" to escape:')
        while(True):
            if(input()=='exit'): break;
    else:
        op = input('Invalid input, try again:[r|m|exit]')
