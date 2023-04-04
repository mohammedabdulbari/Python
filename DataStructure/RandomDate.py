
import datetime
import random

today = datetime.date.today()
given_date = datetime.date(2022, 9, 6)

diff = given_date - today

rand_week = random.randint(0, diff.days//7)
rand_day = random.randint(0, 4)

num_days = rand_week * 7 + rand_day - today.weekday()

new_date = today + datetime.timedelta(num_days)

print('Random Date', new_date)
print('Weekday Number', new_date.weekday())



