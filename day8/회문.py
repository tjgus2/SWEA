# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

t = int(input())

for test_case in range(1, t+1) :
    n, m = map(int, input().split())
    board = [input()  for _ in range(n)]
    result = ""

    # 가로 방향 검사
    for row in board:
        for i in range(n-m+1):
            substr = row[i:i+m]
            if substr == substr[::-1]:
                result = substr

    # 세로 방향 검사
    for col in range(n):
        for i in range(n-m+1):
            substr = ''.join([board[i+j][col] for j in range(m)])
            if substr == substr[::-1]:
                result = substr
                
    print(f"#{test_case} {result}")


