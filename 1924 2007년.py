A = raw_input()
B = A.split()
Month = int(B[0])
Day = int(B[1])
total = 0
Month_Day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(Month):
    total += Month_Day[i]
total += Day
mon = total % 7
if mon == 1:
    print 'MON'
elif mon == 2:
    print 'TUE'
elif mon == 3:
    print 'WED'
elif mon == 4:
    print 'THU'
elif mon == 5:
    print 'FRI'
elif mon == 6:
    print 'SAT'
else:
    print 'SUN'