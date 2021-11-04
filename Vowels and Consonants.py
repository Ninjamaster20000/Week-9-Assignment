text = "hi how are you"
vowel = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"
countV = 0
countC = 0

for i in range(len(text)):
    if text[i] in vowel:
        countV = countV + 1
    elif text[i] in consonant:
        countC = countC + 1

print("Text:", text)
print("Total number of vowels:", countV)
print("Total number of consonants:", countC)