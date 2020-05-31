import sys

def f(n, cur, l, r):
    if len(cur) == n * 2:
        print(cur)
        return
    if l < n:
        f(n, cur + "(", l + 1, r)
    if r < l:
        f(n, cur + ")", l, r + 1)


count = int(sys.stdin.readline().strip())
f(count, '', 0, 0)
