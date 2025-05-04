# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

t = int(input())

for test_case in range(1, t+1):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if grid[i][j] == 0:
                    grid[i][j] = color
                elif grid[i][j] != 0:
                    grid[i][j] = 3 # 빨강 파랑 겹치므로 보라

    count = sum(row.count(3) for row in grid)

    print("#"+str(test_case), count)             