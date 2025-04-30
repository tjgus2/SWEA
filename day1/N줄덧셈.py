# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

n = int(input())
sum = 0

for i in range(1, n+1):
    if (sum < 10000):
        sum += i
print(sum)