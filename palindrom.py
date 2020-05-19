"""
own implementation
In [5]: %timeit palindrom.is_palindrom('qwertyuioppoiuytrewq')
3.25 µs ± 404 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

split/join
In [3]: %timeit palindrom.is_palindrom('qwertyuioppoiuytrewq')
1.43 µs ± 282 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

"""

def is_palindrom(str):
    # left = 0
    # right = len(str) - 1
    # while left < right:
    #     if str[left] != str[right]:
    #         return False
    #     left += 1
    #     right -= 1
    # return True
    return str == "".join(reversed(str))

# import timeit
# print(timeit.timeit("is_palindrom('qwerty1ytrewq')", setup="from __main__ import is_palindrom"))
# assert is_palindrom("qwerty") == False
# assert is_palindrom("qwe") == False
# assert is_palindrom("") == True
# assert is_palindrom("q") == True
# assert is_palindrom("qq") == True
# assert is_palindrom("qwwq") == True
# assert is_palindrom("qwwwwq") == True

