import sys
from collections import Counter

def anagrams(a, b):
    return 1 if Counter(a) == Counter(b) else 0

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
print(anagrams(a,b))
# assert anagrams('qwe', 'ewq') == 1