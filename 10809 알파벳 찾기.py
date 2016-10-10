string_s = input()
check_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
count_list = []
result = ""

for i in check_list:
    try:
        count_list.append(string_s.index(i))
    except ValueError:
        count_list.append(-1)

for i in count_list:
    result += (str(i) + " ")

print(result)