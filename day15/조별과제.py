# 각 테스트 케이스마다, N명의 학생들을 조로 적당히 나누었을 때, 3명 이상의 학생으로 구성된 조의 수의 최댓값을 출력한다.

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    print(f"#{test_case} {n//3}")