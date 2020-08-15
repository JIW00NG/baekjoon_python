# 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651
#
# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.


# 퀵정렬 함수 이용

# def quicksort(x):
#     if len(x) <= 1:
#         return x
#
#     pivot = x[len(x) // 2]
#     less = []
#     more = []
#     equal = []
#     for a in x:
#         if a[1] < pivot[1]:
#             less.append(a)
#         elif a[1] > pivot[1]:
#             more.append(a)
#         else:
#             if a[0] < pivot[0]:
#                 less.append(a)
#             elif a[0] > pivot[0]:
#                 more.append(a)
#             else:
#                 equal.append(a)
#
#     return quicksort(less) + equal + quicksort(more)
#
# import sys
#
# point = []
# for _ in range(int(sys.stdin.readline())):
#     point.append(tuple(map(int, sys.stdin.readline().split())))
#
# for k in quicksort(point):
#     print(*k)


import sys

point = []
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    point.append(tuple((y, x)))

for k in sorted(point):
    print(k[1], k[0])