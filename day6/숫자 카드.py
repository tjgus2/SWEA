# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

# from collections impoort Counter

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    arr = list(map(int, input()))
    
    count_dict = {}
    
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    # count_dict = Counter(arr)

    max_card = -1
    max_count = -1

    for num,cnt in count_dict.items():
        if cnt > max_count or (cnt == max_count and num > max_card):
            max_count = cnt
            max_card = num

    print("#"+str(test_case), max_card, max_count)


