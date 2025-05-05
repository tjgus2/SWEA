# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다. M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.


t = int(input())

for test_case in range(1, t+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_result = float('-inf')
    min_result = float('inf')

    for i in range(N-M+1):
        current_sum = sum(arr[i: i+M])
        max_result = max(current_sum, max_result)
        min_result = min(current_sum, min_result)

    print("#"+str(test_case), max_result-min_result)

# arr = [list(map(int, input().split())) for _ in range(N)] 
# 위는 2차원 배열 입력받는 방법법