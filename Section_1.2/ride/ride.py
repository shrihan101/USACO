"""
ID: shrihan4
LANG: PYTHON3
TASK: ride
"""

f = open('ride.in')
l = f.readlines()

l1 = l[0].strip()
l2 = l[1].strip()
s1 = 1
s2 = 1
for let in l1:
    s1 = s1 * (ord(let) - 64)
for let in l2:
    s2 = s2 * (ord(let) - 64)

f = open('ride.out', 'w')
if s1 % 47 == s2 % 47:
    f.write('GO\n')
else:
    f.write('STAY\n')

f.close()
