import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    A,B=map(int,sys.stdin.readline().split())
    print(A+B)