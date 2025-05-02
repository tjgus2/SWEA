# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    sum = 0

    for i in range(1, n+1):
        if i % 2 == 0:
            sum += -i
        else:
            sum += i

    print("#"+str(test_case), sum)

    # t = int(input())
    # sum = 0