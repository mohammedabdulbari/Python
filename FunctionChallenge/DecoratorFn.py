class NegativeAgeException(Exception):
    pass

def stage(age):
    if age < 0 :
        raise NegativeAgeException('Age should not be Negative')
    elif age >= 0 and age <=12:
        print('Kid')
    elif age >= 13 and age <= 50:
        print('Young')
    elif age >= 51:
        print('Old')

try:
    stage(-160)
except NegativeAgeException as e:
    print(e)
