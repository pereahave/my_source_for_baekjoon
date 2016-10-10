case_number = input()
result_list = []

for i in range(0, int(case_number)):
    test_case = input()
    count_o = 0
    present_score = 1

    for i in test_case:
        if i == "O":
            count_o += present_score
            present_score += 1
        else:
            present_score = 1

    result_list.append(count_o)

for i in result_list:
    print(i)
