import sys

def f(nums):
    max_1 = cur_1 = 0
    for n in nums:
        # assert n in (0,1)
        if n == 1:
            cur_1 += 1
            max_1 = max(max_1, cur_1)
        else:
            cur_1 = 0
    return max_1

if __name__ == "__main__":
    total = int(sys.stdin.readline().strip())

    arr = []
    for _ in range(total):
        arr.append(int(sys.stdin.readline().strip()))
    print(f(arr))
def test_f():
    assert f([]) == 0
    assert f([1]) == 1
    assert f([1, 1, 0]) == 2
    assert f([1, 1]) == 2
    assert f([0, 0, 0, 1]) == 1
    assert f([1, 0, 1, 1, 0, 1, 1, 1]) == 3
