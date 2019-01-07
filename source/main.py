import validateYear as vy

with open("test-dates.txt", 'r') as f:
    for line in f:
        vy.validate(f)