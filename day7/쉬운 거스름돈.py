# S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.

t = int(input())

for test_case in range(1, t+1):
    money = int(input())

    a = b = c = d = e = f = g = h = 0 

    while money >= 50000:
        money -= 50000
        a += 1

    while money >= 10000:
        money -= 10000
        b += 1

    while money >= 5000:
        money -= 5000
        c += 1

    while money >= 1000:
        money -= 1000
        d += 1

    while money >= 500:
        money -= 500
        e += 1

    while money >= 100:
        money -= 100
        f += 1

    while money >= 50:
        money -= 50
        g += 1

    while money >= 10:
        money -= 10
        h += 1

    print("#"+str(test_case))
    print(a, b, c, d, e, f, g, h)