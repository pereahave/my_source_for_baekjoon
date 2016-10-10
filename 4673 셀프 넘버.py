targetlist = []

for i in range(0, 9999, 1):
    targetlist.append(i+1)

def makeselfnumber(N):
    buf1 = str(N)
    result = N
    for i in buf1:
        result += int(i)
    return result

for i in range(0, 9999, 1):
    buf = makeselfnumber(i)
    if targetlist.count(buf) == 0:
        pass
    else:
        targetlist.remove(buf)

for i in targetlist:
    print(i)
