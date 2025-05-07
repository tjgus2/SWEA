# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

t = int(input())

for test_case in range(1, t+1):
    str1 = input()
    str2 = input()

    result = 0

    # for ch in str2:
    #     if ch == str1:
    #         result = 1
    #     else:
    #         result = 0

    if str1 in str2:
        result = 1
    else:
        result = 0

    print("#"+str(test_case), result)