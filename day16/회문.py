# 8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.

for k in range(1, 11):
    n = int(input())
    arr = [input() for _ in range(8)]
    answer = 0

    for i in range(8):
        for j in range(8-n+1):
            if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
                answer += 1

    for j in range(8):
        for i in range(8-n+1):
            col = ''.join(arr[x][j] for x in range(i, i+n))
            if col == col[::-1]:
                answer += 1

    print(f"#{k} {answer}")