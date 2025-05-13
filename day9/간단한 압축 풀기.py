# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    new_str = ""
    
    for _ in range(n):
        c, k = input().split()
        new_str += c * int(k)

    print(f"{test_case}")
    for i in range(0, len(new_str), 10):
        print(new_str[i:i+10])
