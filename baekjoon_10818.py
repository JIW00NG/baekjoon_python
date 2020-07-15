import sys

n=int(sys.stdin.readline())
a_list=list(map(int,sys.stdin.readline().split()))

while len(a_list)!=n:
    a_list=list(map(int,sys.stdin.readline().split()))

print(min(a_list),max(a_list))