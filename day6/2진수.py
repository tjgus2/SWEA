# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고, 13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.

def decimal_to_binary(N):
    result = ''
    count = 0

    # while N > 0:
    #     N *= 2
    #     bit = int(N)
    #     result += str(bit)
    #     N -= bit
    #     count += 1

    #     if count > 12:
    #         return "overflow"
        
    # return result

    while N > 0:
        N *= 2
        bit = int(N)
        result += str(bit)
        N -= bit
        count += 1

        if count > 12:
            return "overflow"
        
    return result

t = int(input())

for test_case in range(1, t+1):
    N = float(input())
    print("#"+str(test_case), decimal_to_binary(N))
