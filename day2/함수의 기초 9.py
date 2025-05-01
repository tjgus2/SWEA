# 인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고 결과를 출력하는 프로그램을 작성하십시오.

def print_longer_string(str1, str2):
    if len(str1) > len(str2):
        return str1
    else:
        return str2

s1, s2 = input().split(",")
print(print_longer_string(s1, s2))