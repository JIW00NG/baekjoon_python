import sys
from functools import reduce

n = int(sys.stdin.readline())

score_list = list(map(int,sys.stdin.readline().split()))

while len(score_list) != n:
    score_list = list(map(int,sys.stdin.readline().split()))

M = max(score_list)
for i in range(n):
    score_list[i] = score_list[i] / M * 100

print(reduce(lambda x, y : x+y, score_list) / n)