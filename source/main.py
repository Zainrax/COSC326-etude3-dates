import validateYear as vy

op = input('Would you like to read date file or manually input a date?[read/manual]\n')
if(op == 'read'): op = 0
elif(op == 'manual'): op = 1

if(op == 0):
    date = input('Enter date:\n')
    vy.validate(date)
elif(op == 1):
    with open("test-dates.txt", 'r') as f:
        for line in f:
            vy.validate(f)
