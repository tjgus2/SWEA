#  다음의 결과와 같이 사용자가 입력한 숫자가 소수인지를 판단하는 프로그램을 작성하십시오. 소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력

# def is_prime(number):
#     for i in range(2, number):
#         if (number % i != 0):
#             print("소수입니다")
#         else:
#             print("소수가 아닙니다")

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i ==0:
            return False
        return True

num = int(input())

if is_prime(num):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")