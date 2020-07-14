import sys

n = int(sys.stdin.readline().rstrip())
star=""

for i in range(2*n-1):
    star=star+"*"

def drawStar(s):
    print(s)
    for i in range(2 * n - 1):
        if i < n-1:
            s = " "+s[:-2]
            print(s)
        elif i >= n:
            s = s[1:] +"**"
            print(s)

drawStar(star)