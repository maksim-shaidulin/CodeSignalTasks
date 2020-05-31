from collections import Counter
import sys

d = Counter()
res = []
cnt = int(sys.stdin.readline().strip())
for _ in range(cnt):
    d += Counter(list(map(int, sys.stdin.readline().strip().split()[1:])))
    # res += sys.stdin.readline().strip().split()[1:]
    # res += map(lambda x: int(x), sys.stdin.readline().strip().split()[1:])
    # sys.stdin.read()
    # d.update(map(lambda x: int(x), sys.stdin.readline().strip().split()[1:]))
    # next_str = sys.stdin.readline().strip().split()[1:]
    # for x in next_str:
    #     d.setdefault(x, 1)
    #     d.update([next_arr)
    # next_arr = [int(x) for x in next_str]
# res.sort(key=lambda x: int(x))
# for x in res:

# for x in sorted(d.elements()):
for x in sorted(d.keys()):
    print(" ".join(str(x) for _ in range(d[x])), end=" ")
    # print(f"{x} ", end='')
# print(" ".join(sorted(d.elements())))
