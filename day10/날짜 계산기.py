# 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.

t = int(input())

for test_case in range(1, t+1):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    m1, d1, m2, d2 = map(int, input().split())
    result = 0

    if m1 == m2:
        result = d2 - d1 + 1
    else:
        result = days[m1] - d1 + 1 + sum(days[m1+1:m2]) + d2

    print(f"#{test_case} {result}")