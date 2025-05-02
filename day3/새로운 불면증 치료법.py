# 호석이는 불면증에 걸렸다. 그래서 잠이 안 올 때의 민간요법 중 하나인 양 세기를 하려고 한다. 호석이는 1번 양부터 순서대로 세는 것이 재미없을 것 같아서 N의 배수 번호인 양을 세기로 하였다. 즉, 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다. 이렇게 숫자를 세던 호석이에게 잠은 더 오지 않고 다음과 같은 궁금증이 생겼다. 이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    seen = [False] * 10
    count = 0 # 곱셈 횟수
    total_seen = 0 # 본 숫자 개수

    while total_seen < 10:
        count += 1
        current = n * count
        temp = current
        while temp > 0:
            digit = temp % 10
            if not seen[digit]:
                seen[digit] = True
                total_seen += 1
            temp //= 10

    print("#"+str(test_case), current)
