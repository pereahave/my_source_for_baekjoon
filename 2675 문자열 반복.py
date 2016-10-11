a = int(input())
for i in range(a):
    c = input()
    b = c.split()
    s_string = ""
    r_iter = 0
    result = ""
    try:
        r_iter = int(b[0])
    except:
        None
        
    try:
        s_string = b[1]
    except:
        None

    if s_string == "":
        None
    else:
        for i in s_string:
            result += r_iter * i
        print(result)
