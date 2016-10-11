a = int(input())
result_list = []

for i in range(a):
    b = int(input())
    result_list.append(b)

result_list.sort()

for i in result_list:
    print(i)
