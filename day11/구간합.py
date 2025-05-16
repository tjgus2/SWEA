t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    current_sum = sum(arr[0:m])
    max_sum = current_sum
    min_sum = current_sum

    for i in range(n-m+1):
        current_sum = sum(arr[i:i+m])
        max_sum = max(max_sum, current_sum)
        min_sum = min(min_sum, current_sum)

    print(f"#{test_case} {max_sum-min_sum}")