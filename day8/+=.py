# 현재 x에 저장된 값은 A, y에 저장된 값은 B이다. 당신은 “x += y” 또는 “y += x” 연산을 원하는 순서대로 원하는 만큼 수행하여, x나 y 둘 중 하나 이상에 저장된 값이 N 초과가 되게 하려고 한다. 연산을 합쳐서 최소 몇 번 수행해야 하는지 계산하는 프로그램을 작성하라.

t = int(input())
for test_case in range(1, t+1):
    a, b, n = map(int, input().split())
    count = 0
    while max(a,b) <= n:
        if a > b :
             b += a
        else:
             a += b
        count += 1
    print(count)