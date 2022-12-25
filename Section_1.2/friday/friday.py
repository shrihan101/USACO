"""
ID: shrihan4
LANG: PYTHON3
TASK: friday
"""

import os

f = open('friday.in')
l = f.readlines()
f.close()
years = int(l[0])
#    m, t, w, t, f, s, s
d = [0, 0, 0, 0, 0, 0, 0]
day = 0
months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
for i in range(years):
    leap = 0
    if (i + 1900) % 4 == 0:
        leap = 1
    if (i + 1900) % 400 != 0 and (i + 1900) % 100 == 0:
        leap = 0
    print("I" + str(i))
    for j in months.keys():
        
        r = 0
        if j == 2 and leap == 1:
            r = 1
            print(months[j] + r)
        for k in range(months[j] + r):
            if k == 12:
                d[day] += 1
            day += 1
            if day >= 7:
                day = 0

f = open('friday.out', 'w')
d_string = ""
d_string += str(d[5]) + " " + str(d[6]) + " " + str(d[0]) + " " + str(
    d[1]) + " " + str(d[2]) + " " + str(d[3]) + " " + str(d[4]) + "\n"
f.write(d_string)

f.close()
