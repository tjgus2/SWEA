# 이름과 나이를 입력 받아 올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.

name = input()
age = int(input())

current_year = 2025
year = current_year + (100 - age)

print(f"{name}(은)는 {year}년에 100세가 될 것입니다.")