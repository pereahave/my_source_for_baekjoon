A = input()
B = input()
C = input()

result = int(A) * int(B) * int(C)
buf = str(result)
count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in buf:
        if i == "0":
                count_list[0] += 1
        if i == "1":
                count_list[1] += 1
        if i == "2":
                count_list[2] += 1
        if i == "3":
                count_list[3] += 1
        if i == "4":
                count_list[4] += 1
        if i == "5":
                count_list[5] += 1
        if i == "6":
                count_list[6] += 1
        if i == "7":
                count_list[7] += 1
        if i == "8":
                count_list[8] += 1
        if i == "9":
                count_list[9] += 1

for i in count_list:
        print(i)
