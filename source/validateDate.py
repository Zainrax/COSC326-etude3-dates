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
    # "validate" function takes an input and uses multiple checks to
    # establish that it is a date in the correct format. The function
    # outputs either a statement that the input was invalid, or the
    # date in the format: "dd first three characters of the month yyyy"

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    date = re.split('-|\s|/', dateIn.strip('\n'))
    datetime.MAXYEAR = 3000
    datetime.MINYEAR = 1753
    invalid = '{} - INVALID: incorrect format used.\nPlease use [d/dd]/[mm/first 3 characters of a month]/[yy/yyyy] seperated with /,-, or <space>, and between 1753 and 3000. eg: "12-SEP-1995","29 02 2000"\n'.format(
        dateIn.strip('\n'))

    if(len(date) > 3):
        return invalid

    try:
        day = int(date[0])
        if not(date[1].isdigit()):
            month = months.index(date[1].capitalize())
        else:
            month = int(date[1])
        year = formatYear(date[2])
    except:
        return invalid

    try:
        datetime.date(year, month, day)
    except ValueError:
        return invalid

    return '{} {} {}\n'.format(day, months[month-1], year)


def formatYear(year):
    # "formatYear" function takes an input, checking that it is a
    # digit, and casting to an int. If value is between 50-99 it will add
    # 1900, else it will add 2000. Else it returns the int casted input.

    if not(year.isdigit()):
        return ValueError
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
