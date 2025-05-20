# 정수 N이 주어질 때, 모든 변의 길이가 N인 가장 넓은 평행사변형의 넓이를 출력하라

t = int(input())

for test_case in range(1,t+1):
    n = int(input())

    print(f"#{test_case} {n*n}")