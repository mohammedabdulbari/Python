
import random
import calendar

week_days = list(calendar.day_name)

random_week_days = [random.randint(0, 6) for i in range(10)]

random_week_names = [week_days[d] for d in random_week_days]

print(random_week_names)
