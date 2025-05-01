# 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.

# def fibonacci(number):
#     if number < 0:
#         return False
#     elif number <= 2:
#         return 1
#     else:
#         return fibonacci(number-1)+fibonacci(number-2)

def fibonacci(n):
    sequence = []
    a, b = 1, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a+b
    return sequence
    
n = int(input())
print(fibonacci(n))