from collections import Counter

def anagrams(a, b):
    # a_set = set(a)
    # b_set = set(b)
    return Counter(a) == Counter(b)

if __name__ == "__main__":
    assert(anagrams('zxc', 'zxc')) == True
    assert(anagrams('zxc', 'cxz')) == True
    assert(anagrams('zxz', 'cxz')) == False
    assert(anagrams('qwe', 'wert')) == False
    assert(anagrams('qwerty', 'qwery')) == False
    assert(anagrams('zxz', '123')) == False
    assert(anagrams('zzz', 'zzz')) == True
    assert(anagrams('zzz', 'zzzz')) == False
    assert(anagrams('zzz', 'zzzz1')) == False
    assert(anagrams('', '')) == True