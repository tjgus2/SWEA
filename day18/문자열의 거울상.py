# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.

t = int(input())

mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

for test_case in range(1, t+1):
    s = input()
    reversed_s = s[::-1]

    mirrored = ""

    for i in range(len(reversed_s)):
        mirrored_char = mirror[reversed_s[i]]
        mirrored += mirrored_char

    print(f"#{test_case} {mirrored}")