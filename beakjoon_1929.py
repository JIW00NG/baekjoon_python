# https://www.acmicpc.net/problem/1929
# 소수 구하기
#
# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.


import sys

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
    print(sieve)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

M, N = map(int, sys.stdin.readline().split())

for i in prime_list(N + 1):
    if i >= M:
        print(i)