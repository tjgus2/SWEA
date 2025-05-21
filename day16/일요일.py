# 오늘의 요일을 나타내는 문자열 S가 주어진다. S는 “MON”(월), “TUE”(화), “WED”(수), “THU”(목), “FRI”(금), “SAT”(토), “SUN”(일) 중 하나이다. 다음 (즉, 내일 이후의 가장 빠른) 일요일까지는 며칠 남았을까?

day_to_index = {
    "MON": 0,
    "TUE": 1,
    "WED": 2,
    "THU": 3,
    "FRI": 4,
    "SAT": 5,
    "SUN": 6
}

t = int(input())

for test_case in range(1, t+1):
    s = input()
    idx = day_to_index[s]
    if idx != 6:
        days_left = 7 - idx - 1
    else:
        days_left = 7

    print(f"#{test_case} {days_left}")