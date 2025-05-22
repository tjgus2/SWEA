# 첫번째 사람부터 N번째 사람까지 각각 쥬스를 얼마씩 마시게 되는지 구하도록 하자.

t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    juice_share = f"1/{n}"

    result = ' '.join([juice_share]*n)

    print(f"#{test_case} {result}")