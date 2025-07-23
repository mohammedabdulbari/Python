# Example With Program
s1 = "listen"
s2 = "silent"

sorted_s1 = sorted(s1)
sorted_s2 = sorted(s2)

print(sorted_s1)  # Output: ['e', 'i', 'l', 'n', 's', 't']
print(sorted_s2)  # Output: ['e', 'i', 'l', 'n', 's', 't']

# Now, comparing the sorted versions
if sorted_s1 == sorted_s2:
    print("Anagrams")
else:
    print("Not Anagrams")

# Output: Anagrams


#This code uses the sorted function to create sorted versions of both strings and
##then checks if these sorted versions are the same. If they are, it means the two 
#strings are anagrams, considering both the length and frequency of characters.






