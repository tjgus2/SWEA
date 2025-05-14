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

    max_result = 0
    for ch in str1:
        if ch in count_dict and count_dict[ch] > max_result:
            max_result = count_dict[ch]

    print(f"#{test_case} {max_result}")

