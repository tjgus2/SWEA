# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

t = int(input())

for test_case in range(1, t+1):
    numbers = list(map(int, input().split()))
    result = 0

    new_num = sorted(numbers)
    for i in range(1, 9):
        result += new_num[i]

    print(f"#{test_case} {round(result/8)}")
