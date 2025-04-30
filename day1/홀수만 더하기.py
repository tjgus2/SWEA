#10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

T = int(input())

for test_case in range(1, T + 1):

    sum = 0
    numbers = map(int, input().split())
    
    for num in numbers:
        if num % 2 == 1:
            sum += num
    
    print("#"+ str(test_case),sum)






