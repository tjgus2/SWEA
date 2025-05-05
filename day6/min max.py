# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_n = float('-inf')
    min_n = float('inf')

    for num in arr:
        if num > max_n:
            max_n = num
        elif num < min_n:
            min_n = num

    print("#"+str(test_case), max_n - min_n)