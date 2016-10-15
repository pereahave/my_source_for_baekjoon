buf1 = int(input()) #자연수 M
buf2 = int(input()) #자연수 N
buf_list = []
output_list = []
check = 1
result_a = 0
result_b = 0

#자연수 M이상 N이하를 가지는 리스트 작성
for i in range(buf1, buf2+1):
    buf_list.append(i)

#소수를 판별하는 함수 작성
def check_number(N):
    if N == 1:
        pass
    else:
        for j in range(1, N):
            check = 1
            if j != 1 and N % j == 0:
                check = 0
                break
        if check == 1:
            return 1
        else:
            return 0

for i in buf_list:
    if check_number(i) == 1:
        output_list.append(i)
    else:
        pass
if output_list:
    for i in output_list:
        result_a += i
    result_b = min(output_list)
    print(result_a)
    print(result_b)
else:
    print(-1)