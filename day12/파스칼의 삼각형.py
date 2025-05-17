t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    triangle = [[1] * (i+1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    print(f"{test_case}")
    for row in triangle:
        print(" ".join(map(str, row)))