import sys

sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")

n, k = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))

_max = 0
for i in range(n):
    current = 0
    for j in range(n):
        if nums[i] <= nums[j] and nums[i] + k >= nums[j]:
            current += 1
    
    _max = max(_max, current)

print(_max)