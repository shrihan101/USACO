import sys
sys.stdin = open('square.in', 'r')
sys.stdout = open('square.out', 'w')

x1, y1, x2, y2 = input().split(' ')
x3, y3, x4, y4 = input().split(' ')

left = min(x1, x3)
right = max(x2, x4)
bottom = min(y1, y3)
top = max(y2, y4)

side = max(int(right) - int(left), int(top) - int(bottom))
print(side ** 2)