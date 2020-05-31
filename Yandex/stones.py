import sys

def f(J, S):
    counter = 0
    for x in S:
        if x in J:
            counter += 1
    return counter


# S = input()
# J = input()
J = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()
print(f(J, S))
# assert f('ab', 'aabc') == 3
# assert f('ab', 'cd') == 0
# assert f('abc', 'aef') == 1
# assert f('', 'aef') == 0
# assert f('abc', '') == 0
# assert f('', '') == 0
# assert f('ab', 'ab') == 2
# assert f('a', 'a') == 1
# assert f('abc', 'a') == 1
