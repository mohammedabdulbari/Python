import re

str1 = ('Time is the most valuable thing we have,'
        ' and once lost, it never returns.')

str2 = ("We never get time back once it's "
    "gone—it's truly the most valuable resource.")

words1 = re.findall(r'\w+', str1.lower())

words2 = re.findall(r'\w+', str2.lower())

wset1 = set(words1)
wset2 = set(words2)

common = wset1 & wset2
unique = wset1 | wset2

ratio = len(common) / len(unique)

print(f"Jaccard Similarity:{ratio:.2f}")

