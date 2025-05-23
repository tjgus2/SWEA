# 0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만드는 것입니다.

for test_case in range(1, 11):
    n, num = input().split()
    stack = []

    for digit in num:
        if stack and stack[-1] == digit:
            stack.pop()
        else:
            stack.append(digit)

    result = ''.join(stack)

    print(f"#{test_case} {result}")