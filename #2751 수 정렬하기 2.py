a = int(input())
result_list = []

for i in range(a):
    b = int(input())
    result_list.append(b)

left_list = []
right_list = []

for i in range(int(len(result_list)/2)):
    left_list.append(result_list[i])
    result_list.remove(result_list[i])

for j in range(len(result_list)):
    right_list.append(result_list[j])
    result_list.remove(result_list[j])
    
print(left_list)
print(right_list)
