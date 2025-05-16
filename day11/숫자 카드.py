from collections import Counter
t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    cards = input()
    count_dict = Counter(cards)

    max_count = max(count_dict.values())
    max_num = max(num for num, cnt in count_dict.items() if cnt == max_count)

    print(f"#{test_case} {max_num} {max_count}")
