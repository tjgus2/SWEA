t = int(input())

for test_case in range(1, t+1):
    str1 = input()
    reversed_str1 = str1[::-1]
    result = 0

    if str1 == reversed_str1:
        result = 1

    print(f"#{test_case} {result}")