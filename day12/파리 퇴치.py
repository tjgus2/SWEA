t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())

    flies = [list(map(int, input().split())) for _ in range(n)]

    max_sum = -1

    for i in range(n-m+1):
        for j in range(n-m+1):
            current_sum = 0
            for x in range(m):
                for y in range(m):
                    current_sum += flies[i+x][j+y]

            if current_sum > max_sum:
                max_sum = current_sum
            
    print(f"#{test_case} {max_sum}")

    
