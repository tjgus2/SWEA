from collections import Counter

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    scroes = list(map(int, input().split()))

    count_dict = Counter(scroes)

    max_freq = 0
    for freq in count_dict.values():
        if freq > max_freq:
            max_freq = freq

    max_scroe = []
    for score, freq in count_dict.items():
        if freq == max_freq:
            max_scroe.append(score)

    result = max_scroe[0]
    for score in max_scroe:
        if score > result:
            result = score

    print(f"#{n} {result}")