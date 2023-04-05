
import datetime

def print_dates(date):
    for i in range(4):
        print(date)
        date += datetime.timedelta(10)


print_dates(datetime.date(200, 1, 15))
