"""
Есть файл, в котором содержаться слова разделённые пробелом. 
Например: "abba com mother bill mother com abba dog abba mother com". 
Нужно найти и вывести тройку слов, которые чаще всего встречаются вместе
 (порядок не имеет значения). То есть в моём примере тройки слов это "abba com mother",
 "com mother bill", "mother bill mother" и т.д. 
 Тут правильным ответом должно быть "abba com mother" (частота — 3 раза).
"""


def find(input):
    res = ""
    d = dict()
    max_key = None
    max_count = 0
    for i in range(len(input) - 2):
        key = tuple(sorted(input[i : i + 3]))
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
        if d[key] > max_count:
            max_count = d[key]
            max_key = key

    return max_key, max_count


string = "abba com mother bill mother com abba dog abba mother com eee"
print(find(string.split()))
