
import calendar

year = int(input('Enter Year: '))

for month in range(1, 13):
    cal = calendar.monthcalendar(year, month)

    first_week = cal[0]
    second_week = cal[1]
    third_week = cal[2]

    if first_week[5] != 0:
        print(second_week[5], '-', month, '-', year)
    else:
        print(third_week[5], '-', month, '-', year)


