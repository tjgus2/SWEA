# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다. 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

t = int(input())

def count_valid_lines(lines, N, K):
    count = 0
    for line in lines:
        consecutive = 0
        for i in range(N + 1):
            if i < N and line[i] == 1:
                consecutive += 1
            else:
                if consecutive == K:
                    count += 1
                consecutive = 0
    return count

for test_case in range(1, t+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
        
    total = count_valid_lines(puzzle, N, K)
    transposed = list(zip(*puzzle))
    total += count_valid_lines(transposed, N, K)

    print("#"+str(test_case), total)


# for _ in range(N):
#    puzzle = list(map(int, input().split()))
# puzzle을 행마다 받는데 누적하지 않음
# puzzle = [list(map(int, input().split())) for _ in range(N)]

# transposed = list(zip(*puzzle))
# 세로줄 리스트를 가로줄 리스트로 변환하는 방법