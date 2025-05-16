t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    grid = [[0]*10 for _ in range(10)]
    
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if grid[i][j] == 0:
                    grid[i][j] = color
                elif grid[i][j] != color:
                    grid[i][j] = 3

    purple_count = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                purple_count += 1
    
    print(f"#{test_case} {purple_count}")