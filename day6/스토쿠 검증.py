# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

def check_sudoku(puzzle):
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            row.add(puzzle[i][j])
            col.add(puzzle[j][i])
        if len(row) != 9 or len(col) != 9:
            return 0
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = set()
            for x in range(3):
                for y in range(3):
                    block.add(puzzle[i+x][j+y])

            if len(block) != 9:
                return 0
    return 1

t = int(input())

for test_case in range(1, t+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    print("#"+str(test_case), check_sudoku(puzzle))

# 1. 각 행과 열을 확인
# 2. 3X3 격자 체크
# set을 사용하는 이유: 중복을 자동으로 제거해주기 때문에