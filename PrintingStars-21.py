import sys

num = int(sys.stdin.readline().rstrip())

def drawStar(n):

    for i in range(n):
        print("*",end="")

        if n%2!=0:
            for j in range(n//2):
                print(" *",end="")
            print()
            for j in range(n//2):
                print(" *",end="")
            print()
        else:
            for j in range(n//2-1):
                print(" *",end="")
            print()
            for j in range(n//2):
                print(" *",end="")
            print()


drawStar(num)