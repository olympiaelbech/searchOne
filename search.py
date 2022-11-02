import sys

# Given a sorted list 'a', and an element 'x' to
#search for, return True if x is in the array

def search(a, x):
    lo = 0
    hi = len(a) - 1
    while lo <= hi: # range is non-empty
        mid = (lo + hi) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            lo = mid + 1 
        else:
            hi = mid - 1
    return False # not found

f = open('words')
words = []
for word in f:
    words.append(word.strip())
s = input('Word to find: ')
if search(words, s):
    print('found')
else:
    print('not found')