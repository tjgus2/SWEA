#1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

n = int(input())

for i in range(n+1):
    print(2**i, end=" ")