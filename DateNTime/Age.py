
from datetime import date


def age(dob):

    today = date.today()

    years = today.year - dob.year

    if (today.month , today.day) < (dob.month, dob.day):
        years -= 1

    return years


print('Age:', age(date(2000, 7, 1)))
