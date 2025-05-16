t = int(input())

for test_case in range(1, t+1):
    n = float(input())
    s_count = ""

    for _ in range(12):
        n *= 2
        if n >=1.0:
            s_count += "1"
            n -= 1.0
        else:
            s_count += "0"
        if n == 0.0:
            break
    else:
        print(f"#{test_case} overflow")
        continue

    print(f"#{test_case} {s_count}")
        