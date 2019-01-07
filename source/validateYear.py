import re

def validate(dateIn):
    months = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':30,'Jun':31,'Jul':31,'Aug':30,'Sep':31,'Oct':30,'Nov':31,'Dec':31}
    date = re.split('-|\s|/', dateIn)
    if((len(date) < 3) | len(date) > 3): 
        return '{} - INVALID: incorrect format.\nPlease use dd/[mm/3 chars for month]/[yy/yyyy] seperated with "/","-", or <space>, eg: 12-SEP-1995'.format(dateIn)
    day = int(date[0])
    month = formatMonth(date[1])
    year = formatYear(date[2])
    errors = []

    if(month != 'err'):
        if (day.isDigit()):
            if((day > months[month]) & (day > 0)):
                err = True
                if(isLeapYear(year) & (month == 'Feb') & (day == 29)):
                    err = False
                if(err): 
                    errors.append('days out of range')
        else:
            errors.append('invalid day format(use: dd)')
    else:
        errors.append('unable to validate day')
    
    if(month == 'err'):
        errors.append('not a valid month')

    if(year.isDigit()):
        if((year < 1753) | (year > 3000)):
            errors.append('year out of range')
    else:
        errors.append('invalid year format(use: yy/yyyy)')
    
    if(len(errors) >= 1):
        return '{} - INVALID: {}'.format(dateIn, ", ".join(errors).capitalize() + ".")
    else:
        return '{} {} {}'.format(day,month,year)
    
            
def isLeapYear(year):
    if ((year % 4 == 0) & (year % 100 == 0) & (year % 400 == 0)):
        return True;
    else:
        return False

def formatMonth(month):
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    if (month.isdigit()):
        month = int(month)
        if((month > 12) | (month <= 0)): return 'err'
        return months[month]
    elif(month.capitalize() in months):
        return month.capitalize()
    else:
        return 'err'

def formatYear(year):
    if not(year.isDigit()): return 'err'
    year = int(year)
    if(year <= 99):
        if(year >= 50):
            year += 1900
            return year
        else:
            year += 2000
            return year
    else:
        return year

with open("test-dates") as f:
    for line in f:
        print(validate(line))