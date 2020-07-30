# 소수 찾기
#
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
#
# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

import sys


def primenum(n):
    if n == 1 or (n != 2 and n % 2 == 0) or (n != 3 and n % 3 ==0) or (n != 5 and n % 5 == 0) or (n != 7 and n % 7 == 0):
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
while len(num_list) != N:
    num_list = list(map(int, sys.stdin.readline().split()))

count = 0
for j in num_list:
    if primenum(j):
        count = count + 1

print(count)
