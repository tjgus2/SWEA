t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    result = 0

    arr = list(map(int, input().split()))
    arr.sort()

    for i in range(n):
        result = arr[n-1] - arr[0]

    print(f"#{test_case} {result}")