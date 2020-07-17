import sys

def score(str):
    total_score=0
    count=0
    for i in range(len(str)):
        if str[i]=="O":
            count+=1
            total_score+=count
        elif str[i]=="X":
            count=0
        else:
            break

    return total_score

n=int(sys.stdin.readline())

for i in range(n):
    print(score(sys.stdin.readline()))

