t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = []

    if n>m:
        for i in range(n-m+1):
            temp = 0
            for j in range(m):
                temp += a[i+j] * b[j]
            result.append(temp)
    
    else:
        for i in range(m-n+1):
            temp = 0
            for j in range(n):
                temp += a[j] * b[i+j]
            result.append(temp)

    print(f"#{test_case} {max(result)}")