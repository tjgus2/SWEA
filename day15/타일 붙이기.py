T = int(input())  # 테스트 케이스 수

for test_case in range(1, T + 1):
    N = int(input())  # 2xN 크기의 공간

    dp = [0] * (N + 1)
    dp[0] = 1  # 초기값 설정
    if N >= 1:
        dp[1] = 1
    if N >= 2:
        dp[2] = 3
    if N >= 3:
        dp[3] = 6

    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2] + dp[i - 3]

    print(f"#{test_case} {dp[N]}")
