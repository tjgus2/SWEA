# 입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를 게임 규칙에 맞게 출력하는 프로그램을 작성하라. 박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.

n = int(input())

for i in range(1, n+1):
    num_str = str(i)
    clap_count = 0

    for ch in num_str:
        if ch in '369':
            clap_count += 1

    if clap_count == 0:
        print(i, end=" ")
    else:
        print("-"*clap_count, end=" ")