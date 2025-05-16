t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(n)]
    
    result = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                count += 1
            else:
                if count == k:
                    result += 1
                count = 0
        if count == k:
            result += 1

    for j in range(n):
        count = 0
        for i in range(n):
            if puzzle[i][j] == 1:
                count += 1
            else:
                if count == k:
                    result += 1
                count = 0
        if count == k:
            result += 1

    print(f"#{test_case} {result}")

    
