# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    print("#"+str(test_case), *arr)

    # *arr는 리스트 arr = [1, 2, 3]을 1 2 3처럼 요소를 각각 꺼내서 출력함