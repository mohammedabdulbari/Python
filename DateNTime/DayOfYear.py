

import datetime

str_date = input('Enter Date in DD-MM-YYYY: ')
d, m, y = str_date.split('-')

d1 = datetime.date(int(y), int(m), int(d))
first_day = datetime.date(int(y), 1, 1)

diff = d1 - first_day

print('Day Number:', diff.days + 1)
