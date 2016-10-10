buf1 = input()
buf2 = int(buf1) + 1
target_list = []

def check_asn(N):
    buf = str(N)
    if len(buf) == 1:
        return 1
    elif len(buf) == 2:
        return 1
    else:
        buf3 = int(buf[0]) - int(buf[1])
        buf4 = int(buf[1]) - int(buf[2])
        if buf3 == buf4:
            return 1
        else:
            return 0


for i in range(1, buf2):
    if check_asn(i) == 1:
        target_list.append(i)
    else:
        pass

print(len(target_list))
