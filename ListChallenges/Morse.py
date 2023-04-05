
codes  = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

text = 'deface'

morse_str=''

for x in text:
    morse_str += codes[ord(x)-97] + " "

print(morse_str)
