# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.

t = int(input())

for test_case in range(1, t+1):
    a1, b1, a2, b2 = map(int, input().split())
    result1 = 0
    result2 = 0

    if a1+a2 > 12:
        result1 = (a1 + a2) - 12
    else:
        result1 = a1 + a2

    if b1+b2 > 60:
        result2 = (b1 + b2) - 60
        result1 += 1
    else:
        result2 = b1 + b2

    print("#"+str(test_case), result1, result2)