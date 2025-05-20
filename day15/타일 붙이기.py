# 2x1, 2x2, 2x3 크기의 타일을 2xN 크기의 공간에 붙이려고 한다. N이 주어지면 붙이는 방법이 모두 몇 가지가 경우가 있는지 출력하는 프로그램을 만드시오.

t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    dp = [0]* (n+1)
    dp[0] = 1

    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 3
    if n >= 3:
        dp[3] = 6

    for i in range(4, n+1):
        dp[i] = dp[i-1] + 2*dp[i-2] + dp[i-3]

    print(f"#{test_case} {dp[n]}")