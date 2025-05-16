t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    r1, c1, r2, c2, color = map(int, input().split())

    for i in range(r1):
        for j in range(c1):
            grid[i][j] = color
    
    for a in range(r2):
        for b in range(c2):
            grid[i][j] = color

    count = 0
    for i in range(r1):
        for j in range(c2):
            if grid[i][j] >