# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다. 죽은 파리의 개수를 구하라!

t = int(input())

for test_case in range(1, t+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for x in range(M):
                for y in range(M):
                    total += array[i+x][j+y]
            max_flies = max(total, max_flies)

    print("#"+str(test_case), max_flies)
