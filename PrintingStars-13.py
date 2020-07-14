import sys

n = int(sys.stdin.readline().rstrip())
star = ""

for i in range(2 * n - 1):
    if i < n:
        star = star + "*"
    elif i >= n:
        star = star[:-1]
    print(star)
