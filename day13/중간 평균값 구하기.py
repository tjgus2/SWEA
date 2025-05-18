t = int(input())

for test_case in range(1, t+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    numbers.pop(0)
    numbers.pop(-1)

    avg = sum(numbers) / len(numbers)
    
    print(f"#{test_case} {round(avg)}")