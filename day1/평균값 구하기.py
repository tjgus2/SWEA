#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라. (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())

for test_case in range(1, T+1):
    n = list(map(int, input().split()))

    total = sum(n)
    avg = total/10

    print("#"+str(test_case), round(avg))
