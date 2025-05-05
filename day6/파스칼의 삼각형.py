# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    triangle = [[1] * (i+1) for i in range(n)]

    for i in range(2,n): # 2번째 줄부터 시작
        for j in range(1, i): # 양끝은 1
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    print("#"+str(test_case))
    for row in triangle:
        print(" ".join(map(str, row)))