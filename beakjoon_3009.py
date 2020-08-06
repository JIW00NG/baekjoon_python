# # 네 번째 점
# # https://www.acmicpc.net/problem/3009
# #
# # 문제
# # 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# #
# # 입력
# # 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
# #
# # 출력
# # 직사각형의 네 번째 점의 좌표를 출력한다.

# 직접 풀었을 떄
import sys

X = [0] * 3
Y = [0] * 3
for i in range(3):
    X[i], Y[i] = map(int,sys.stdin.readline().split())

resultx = []
resulty = []
for i in range(3):
    resultx.append(2 * sum(list(set(X))) // 2 - X[i])
    resulty.append(2 * sum(list(set(Y))) // 2 - Y[i])

for i in list(set(X)):
    resultx.remove(i)
for i in list(set(Y)):
    resulty.remove(i)

print(resultx[0], resulty[0])

# 이상적인 답
# a, b = map(int, input().split())
# c, d = map(int, input().split())
# e, f = map(int, input().split())
# print(a ^ c ^ e, b ^ d ^ f)