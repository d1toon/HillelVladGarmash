import string

start, end = input().split('-')
letters = string.ascii_letters
print(letters[letters.index(start):letters.index(end)+1])
