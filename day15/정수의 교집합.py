# 두 그룹에 모두 들어있는 정수의 개수를 알아내는 프로그램
from collections import Counter

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))

    c_n = Counter(n_arr)
    c_m = Counter(m_arr)

    common_count = 0
    
    for num in c_n:
        if num in c_m:
            common_count += min(c_n[num], c_m[num])

    print(f"#{test_case} {common_count}")