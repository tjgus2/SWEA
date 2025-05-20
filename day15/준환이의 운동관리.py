# 당신은 준환이가 제한되어 있는 시간을 넘은 운동을 한 것인지, 그것이 아니라면 몇 분 더 운동을 해야 제한을 맞출 수 있는지 출력하는 프로그램을 작성해야 한다.

t = int(input())

for test_case in range(1, t+1):
    l, u, x = map(int, input().split())

    if l > x:
        result = l-x
    elif x > u:
        result = -1
    else:
        result = 0

    print(f"#{test_case} {result}")