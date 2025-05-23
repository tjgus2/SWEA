# 다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.
#- 8개의 숫자를 입력 받는다.

#- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

# 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

t = 10

for test_case in range(1, t+1):
    _ = input()
    numbers = list(map(int, input().split()))

    while True:
        for i in range(1, 6):
            num = numbers.pop(0) -i
            if num <= 0:
                numbers.append(0)
                break
            else:
                numbers.append(num)
        else:
            # for문이 break 없이 정상 종료했을 때 계속 while문 진행
            continue
        # for문에서 break 발생하면 이 부분 실행(while문 종료)
        break


    print(f"#{test_case}", *numbers)

