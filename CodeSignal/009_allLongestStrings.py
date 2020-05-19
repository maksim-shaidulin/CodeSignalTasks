def allLongestStrings(inputArray):
    from collections import defaultdict

    dt = defaultdict(list)
    max_length = 0
    for value in inputArray:
        max_length = max(max_length, len(value))
        dt[len(value)].append(value)

    return dt[max_length]


inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(inputArray))
