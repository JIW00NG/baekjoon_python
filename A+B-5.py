import sys

def hap():
    A,B=map(int,sys.stdin.readline().split())
    print(A+B)

while 1:
    try:
        hap()
    except:
        break