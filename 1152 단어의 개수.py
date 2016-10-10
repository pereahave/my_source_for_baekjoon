bufA = input()
count_word = 1

if bufA == "": #입력이 없으면 0를 출력
    print(0)
else:
    for i in bufA:
        if i == " ": #공백문자를 계산
            count_word += 1
    if bufA[-1] == " ": #마지막 글자가 공백이라면
        count_word -= 1
    if bufA[0] == " ": #첫 글자가 공백이라면
        count_word -= 1
    print(count_word)