
s1 = input('Enter a String')
s2 = input('Enter second String')

if len(s1) != len(s2):
    print('Not Anagram')
else:

    for x in s1:
        if x not in s2:
            print('Not Anagarm')
            break;
    else:
        print('Anagram')
