# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

t = int(input())

for test_case in range(1, t+1):
    str1 = input()
    str2 = input()

    count_dict = {}

    for ch in str2:
        if ch in count_dict:
            count_dict[ch] += 1
        else:
            count_dict[ch] = 1

    max_count = 0

    for ch in str1:
        if ch in count_dict and count_dict[ch] > max_count:
            max_count = count_dict[ch]

    print("#"+str(test_case), max_count)