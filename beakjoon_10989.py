# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
#
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

print(num_list)
while len(num_list) > 0:
    print(min(num_list))
    num_list.remove(min(num_list))