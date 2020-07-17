import sys

num_list=[]
divide_num=42

for i in range(10):
    num_list.append(int(sys.stdin.readline())%divide_num)

print(len(list(set(num_list))))
