# 다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한 팩토리얼 값을 구하는 프로그램을 작성하십시오.

def factorial(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
print(factorial(n))