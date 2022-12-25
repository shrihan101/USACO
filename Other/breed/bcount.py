import sys

sys.stdin = open('bcount.in', 'r')
sys.stdout = open('bcount.out', 'w')

N, Q = map(int, input().split())
breeds = []
queries = []

for i in range(N):
    breeds.append(int(input()))

for i in range(Q):
    one, two = map(int, input().split())
    queries.append((one, two))

for q in queries:
    start = q[0] - 1
    end = q[1]
    b1 = 0 # number of holsteins
    b2 = 0 # number of guernseys
    b3 = 0 # numbeer of jerseys
    for i in range(start, end):
        if breeds[i] == 1:
            b1 += 1
        if breeds[i] == 2:
            b2 += 1
        if breeds[i] == 3:
            b3 += 1
        
    print(b1, b2, b3)
