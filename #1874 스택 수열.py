output_list = []
buf_max = 0

a = int(input()) #숫자 몇 개를 입력받는가?
for i in range(a):
    b = int(input())
    if b < buf_max:
        output_list.append(
