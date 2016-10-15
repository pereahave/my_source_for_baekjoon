n = int(input())
input_list = input()
buf1_list = input_list.split()
buf2_list = []
output_number = 0
check = 0

for i in buf1_list:
    buf2_list.append(int(i))

for i in buf2_list:
    if i == 1:
        pass
    else:
        for j in range(1, i):
            check = 1
            if j != 1 and i % j == 0:
                check = 0
                break
        if check == 1:
            output_number += 1

print(output_number)
