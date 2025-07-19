
import re

def panrgam(phrase):
    letters = re.sub(r'[^a-zA-Z]', '', phrase)
    letter_set = set(letters.lower())
    if len(letter_set) == 26:
        return True
    else:
        return False

str = 'The quick brown fox jumps over the lazy dog'

print(panrgam(str))
