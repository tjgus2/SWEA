# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

t = int(input())

for test_case in range(1, t+1):
    word = input()

    reverse_word = word[::-1]

    if word == reverse_word:
        ans = 1
    else: 
        ans = 0

    print("#"+str(test_case), ans)