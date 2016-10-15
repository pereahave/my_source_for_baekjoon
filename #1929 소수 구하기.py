import math

buf1 = input()
buf2 = buf1.split()
m = int(buf2[0]) #작은수
n = int(buf2[1]) #큰수
candidates = []

for i in range(m, n+1):
    candidates.append(i)

