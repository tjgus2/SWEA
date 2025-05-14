t = int(input())

for test_case in range(1, t+1):
    str_1 = input()
    stack = []

    for ch in str_1:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    print(f"#{test_case} {len(stack)}")
