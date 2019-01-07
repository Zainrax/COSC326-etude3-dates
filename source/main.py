import validateYear as vy

op = input('Would you like to read(r) date file or manually(m) input a date?read="r"|manual="m"\n')


if(op == 'm'):
    date = input('Enter date:\n')
    print(vy.validate(date))
elif(op == 'r'):
    with open("test-dates.txt", 'r') as f:
        for line in f:
            print(vy.validate(line))
