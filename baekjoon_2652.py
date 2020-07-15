import sys

n_list=[]

for i in range(9):
    n_list.append(int(sys.stdin.readline()))

print(max(n_list))
print(n_list.index(max(n_list))+1)