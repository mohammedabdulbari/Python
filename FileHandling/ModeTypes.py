
file = open('ModeDemo.txt', 'r+')
str1=file.read(10)
print(str1)

file.write('Good Bye')
file.close()