# 정렬된 숫자를 가진 리스트에서 특정 숫자를 찾는 함수를 정의하고,이 함수를 이용해 임의의 숫자의 포함 여부를 출력하는 프로그램을 작성하십시오.

def number(lst, n):
    for item in lst:
        if n in lst:
            return f"{n} => True"
        else:
            return f"{n} => False"
        
lst = [2, 4, 6, 8, 10]
print(lst)
print(number(lst, 5))
print(number(lst, 10))
