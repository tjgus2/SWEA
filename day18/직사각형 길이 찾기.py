# 직사각형의 네 변 중에서 세 변의 길이가 주어진다. 나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라.

from collections import Counter

t = int(input())

for test_case in range(1, t+1):
    a, b, c = map(int, input().split())

    count = Counter([a, b, c])

    for key, value in count.items():
        if value == 1:
            print(f"#{test_case} {key}")
            break