#10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

t = int(input())

for test_case in range(1, t+1):
    numbers = list(map(int, input().split()))

    print("#"+str(test_case), max(numbers))