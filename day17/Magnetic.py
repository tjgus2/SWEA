# 같은 테이블에서 일정 간격을 두고 강한 자기장을 걸었을 때, 시간이 흐른 뒤에 자성체들이 서로 충돌하여 테이블 위에 남아있는 교착 상태의 개수를 구하라.

for test_case in range(1, 11): 
    n = int(input())
    mag = [list(map(int, input().split())) for _ in range(100)]
    count = 0
    
    for i in range(n):
        state = 0
        for j in range(n):
            cell = mag[j][i]
            if cell == 1:
                state = 1
            elif cell == 2:
                if state == 1:
                    count += 1
                    state = 0

    print(f"#{test_case} {count}")
