import sys
from functools import reduce

score_list=[]

for i in range(5):
    score=int(sys.stdin.readline())
    if score<40:
        score=40

    score_list.append(score)

total=int(reduce(lambda x,y:x+y,score_list)/5)
print(total)