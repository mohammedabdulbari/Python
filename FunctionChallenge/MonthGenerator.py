import calendar

def next_month():
    count = 1
    while True:
        name = calendar.month_name[count]
        yield name
        count = count % 12 + 1


m = next_month()

print(next(m))
print(next(m))
