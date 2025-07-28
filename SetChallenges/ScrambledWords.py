
word_set = {'plea', 'medical', 'listen', 'leap', 'decimal'
    , 'silent', 'pale', 'enlist'}

result = set()

print("Scrambled word pairs:")

for word1 in word_set:
    for word2 in word_set:
        if word1 != word2 and sorted(word1) == sorted(word2):
            pair = tuple(sorted((word1, word2)))
            result.add(pair)

for pair in result:
    print(pair)

