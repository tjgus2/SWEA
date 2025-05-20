# 아기 석환이 두 정수를 곱셈할 수 있으면 곱을 출력하고, 아니면 -1을 출력하라.

t = int(input())

for test_case in range(1, t+1):
    a, b = map(int, input().split())

    result = a*b

    if (a >= 10 or b >= 10):
        result = -1

    print(f"#{test_case} {result}")
    