t = int(input())

for test_case in range(1, t+1):
    P, Q, R, S, W = map(int, input().split())
    ans = 0

    a = P * W
    if (W <= R):
        b = Q
    else:
        b = Q + (W-R) * S

    if a > b:
        ans = b
    else:
        ans = a

    print("#"+str(test_case), ans)