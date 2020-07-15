import sys
from functools import reduce

n_list=[]
count=[0 for i in range(10)]

for i in  range(3):
    n_list.append(int(sys.stdin.readline()))

multi=reduce(lambda x,y:x*y,n_list)

def division(n):
    for i in range(len(str(n))):
        if n%10==0:
            count[0] += 1
        elif n%10==1:
            count[1] += 1
        elif n%10==2:
            count[2] += 1
        elif n%10==3:
            count[3] += 1
        elif n%10==4:
            count[4] += 1
        elif n%10==5:
            count[5] += 1
        elif n%10==6:
            count[6] += 1
        elif n%10==7:
            count[7] += 1
        elif n%10==8:
            count[8] += 1
        elif n%10==9:
            count[9] += 1
        n//=10

division(multi)

for i in range(10):
    print(count[i])