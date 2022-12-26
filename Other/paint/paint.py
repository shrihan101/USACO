import sys

sys.stdin = open('paint.in', 'r')
sys.stdout = open('paint.out', 'w')

a, b = input().split()
c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
total = (b-a) + (d-c)

ab = list(range(a, b+1))
cd = list(range(c, d+1))

covered = len(set(ab) & set(cd))
total -= covered

if covered != 0:
    total += 1

print(total)