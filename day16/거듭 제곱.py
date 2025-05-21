# 두 개의 숫자 N, M이 주어질 때, N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현해 보아라.

def power(n, m):
    if m == 0:
        return 1
    return n*power(n, m-1)

for _ in range(10):
    t = int(input())
    n, m = map(int, input().split())
    result = power(n, m)
    print(f"#{t} {result}")