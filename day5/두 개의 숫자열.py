# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    total = -float('inf')

    if n >= m:
        for a in range(n-m+1):
            temp = 0
            for b in range(m):
                temp += A[a+b] * B[b]
            total = max(total, temp)

    else:
        for a in range(m-n+1):
            temp = 0
            for b in range(n):
                temp += A[b] * B[a+b]
            total = max(total, temp)

    print("#"+str(test_case), total)

# temp += A[a+b] * B[b]
# temp += A[b] * B[a+b]
# 위 코드는 슬라이딩 윈도우(이동하면서 비교하는 방식)에서 자주 등장하는 패턴

# total = -float('inf')
# 최댓값을 구할 때 초기값으로 사용됨
# total = float('inf')
# 최솟값을 구할 때 초기값으로 사용됨