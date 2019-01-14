import re
import datetime
"""
Library containing functions for validating a date.
Used to validate dates between the years 1753 and 3000,
and is based around the gregorian calender.
The dates are checked against the format:
[d/dd]/[0m/m/mm/first 3 characters of month]/[yy/yyy]
separted by '/','-', or <space>
eg. 29/Feb/2000

Author: Patrick Baxter(baxpa469)
Date: 8/01/2019
"""


def validate(dateIn):
    """Checks that an input is a date in the correct format. 

    Args:
        dateIn: A date between 1753 and 3000.
    Returns:
        The input date formated or an invalid response
    """
    dateIn = dateIn.strip('\n')
    date = re.split('-|\\s|/', dateIn)
    if not(len(date) == 3):
        return '{} - INVALID: {}'.format(dateIn, "Must have 3 values seperated using '/','-', or <space>.")
    errors = []
    day = date[0]
    month = date[1]
    year = date[2]

    try:
        month = format_month(month)
    except ValueError:
        month = 'err'
        errors.append("invalid month used")

    try:
        year = format_year(date[2])
        if((year > 3000)|(year < 1753)):
            year = 'err'
            errors.append("year out of range")
    except ValueError:
        year = 'err'
        errors.append("invalid year used")

    if((month == 'err')|(year == 'err')):
        errors.append('unable to verify day')
    elif (day.isdigit()):
        day = format_day(int(day), month, year)
        if(day == 'err'):
            errors.append("invalid day used")
    else:
        errors.append("days must be a digit")
    
    if(len(errors) >= 1):
        return '{} - INVALID: {}'.format(dateIn, ", ".join(errors).capitalize() + ".")
    else:
        day = "0" + str(day) if day < 10 else day
        return '{} {} {}'.format(day,month,year)

def isLeapYear(year):
    """Checks that a year is a leap year

    Args:
        year: user input year
    Returns:
        Boolean depending if it is a leap year or not.
    """
    if ((year % 4 == 0) & (year % 100 == 0) & (year % 400 == 0)):
        return True
    else:
        return False

def format_day(day, month, year):
    """Checks a day within the month ranges and depending if it a leap year

    Args:
        day: user input day
    Returns:
        returns the day if it is valid.
    """
    months = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':30,'Jun':31,
              'Jul':31,'Aug':30,'Sep':31,'Oct':30,'Nov':31,'Dec':31}
    if(isLeapYear(year)):
        months['Feb'] = 29
    if((day <= months[month]) & (day > 0)):
        return day
    else:
        return 'err'

def format_month(month):
    """Formats a month to first 3 characters of the month input

    Args:
        month: user input month
    Returns:
        A ValueError if the input is not a month, or a 3 character month.
    """
    months = ['Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec']
    if (month.isdigit()):
        month = int(month)
        if((month > 12) | (month <= 0)): raise ValueError
        return months[month - 1]
    elif(month.capitalize() in months):
        return month.capitalize()
    else:
        raise ValueError

def format_year(year):
    """Formats a year to a "yyyy" format if input is less than 100.

    Args:
        year: user input year
    Returns:
        A ValueError if the input is not a digit, or the year in yyyy format.
    """
    if not(year.isdigit()):
        raise ValueError
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

