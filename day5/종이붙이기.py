# 10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오

t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[10] = 1

    for i in range(20, n+1, 10):
        dp[i] = dp[i-10] + dp[i-20]

    print("#"+str(test_case), dp[n])

# dp 다이나믹 프로그래밍으로 풀어야 함.. 해결 못한 문제