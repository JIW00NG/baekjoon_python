import sys

N,X=map(int,sys.stdin.readline().split())

n_list=list(map(int,sys.stdin.readline().split()))

for i in range(N):
    if n_list[i]<X:
        print(n_list[i],end=" ")
