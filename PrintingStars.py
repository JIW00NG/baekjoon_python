import sys

n=int(sys.stdin.readline().rstrip())

for i in range(n):
    star="*"
    for j in range(n-1-i):
        star=" "+star
    for j in range(i):
        star=star+"*"
    print(star)
