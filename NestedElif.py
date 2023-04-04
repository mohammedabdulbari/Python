john = float(input("Enter John's age"))
smith = float(input("Enter Smith's age"))
ajay = float(input("Enter Ajay's age"))

if john > smith and john > ajay:
    print('John is elder')
elif smith > ajay:
    print('Smith is elder')
else:
    print('Ajay is elder')
