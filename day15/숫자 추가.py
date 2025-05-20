# 완성된 수열에서 인덱스 L의 데이터를 출력하는 프로그램을 작성하시오.

t = int(input())

for test_case in range(1, t+1):
    n, m, l = map(int, input().split())
    # n: 수열의 길이 m: 추가 횟수 l: 출력할 번호
    numbers = list(map(int, input().split()))
    
    for _ in range(m):
        a, b = map(int, input().split())
        numbers.insert(a, b)
        
    print(f"#{test_case} {numbers[l]}")