
import datetime


str_date = input('Enter Date in DD-MM-YYYY format:')

d, m, y = str_date.split('-')

d1 = datetime.date(int(y), int(m), int(d))

print('Date:', d1)

