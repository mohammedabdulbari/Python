

file = open('MyData.txt', 'w')
str1 = file.read(6)
print(str1)
str1= file.read(10)
print(str1)
print(type(file))