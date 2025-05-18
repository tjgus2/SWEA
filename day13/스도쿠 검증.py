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
    puzzle = [list(map(int, input().split()))for _ in range(9)]

    result = check_sudoku(puzzle)
    print(f"#{test_case} {result}")
    