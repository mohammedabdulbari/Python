
hours = input('Enter Hours separated by spaces:')
wage = int(input('Enter Hourly Wage:'))

hours = hours.split()

week_hours = [int(x) for x in hours]

total_hrs = sum(week_hours)

if total_hrs <= 40:
    tot_wages = total_hrs * wage
else:
    overtime = total_hrs - 40
    tot_wages = 40 * wage + overtime * wage * 1.5

print('Total Wages:', tot_wages)
