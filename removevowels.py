'''def rmvowel( sentence):
    return [i for i in sentence if i in 'aeiou']

sentence = "This life is awesome"
print(list(rmvowel (sentence)))'''

def disemvowel(word):
    vowels = set('AEIOU')
    new_letters = [letter for letter in word if letter.upper() not in vowels]
    print(''.join(new_letters))

print(disemvowel("This life is awesome"))