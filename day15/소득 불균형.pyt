# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.

t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    money = list(map(int, input().split()))
    avg_m = sum(money)//n
    count = 0

    for i in range(n):
        if avg_m >= money[i]:
            count += 1

    print(f"#{test_case} {count}")