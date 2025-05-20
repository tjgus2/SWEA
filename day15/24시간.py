# 지금은 자정에서부터 정확히 A시간이 지났다. 앞으로 정확히 B시간이 더 지난다면, 24시간제 시계에서 그 때는 몇 시일까?

t = int(input())

for test_case in range(1, t+1):
    a, b = map(int, input().split())
    result = a + b

    if result == 24:
        result = 0
    elif result > 24:
        result -= 24

    print(f"#{test_case} {result}")