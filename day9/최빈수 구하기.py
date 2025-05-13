# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

from collections import Counter
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    scores = list(map(int, input().split()))

    count_dict = Counter(scores)
    
    max_freq = 0
    for freq in count_dict.values():
        if freq > max_freq:
            max_freq = freq

    max_score = []

    for score, freq in count_dict.items():
        if freq == max_freq:
            max_score.append(score)

    result = max_score[0]
    for score in max_score:
        if score > result:
            result = score

    print(f"#{n} {result}")