# 두 사람이 만든 단어장에 공통으로 들어있는 단어의 개수를 알아내는 프로그램을 만드시오

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())

    words_n = set(input() for _ in range(n))
    words_m = set(input() for _ in range(m))

    common = words_m & words_n

    print(f"#{test_case} {len(common)}")