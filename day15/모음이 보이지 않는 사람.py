# 불의의 교통사고를 당한 당신은 얼마 후 자신의 인식 속에서 모음이라는 것이 사라진 것을 알게 되었다.

t = int(input())

for test_case in range(1, t+1):
    input_str = input()
    vowels = "aeiou"
    result = ""

    for ch in input_str:
        if ch not in vowels:
            result += ch

    print(f"#{test_case} {result}")