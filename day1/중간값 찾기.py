#입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

n = int(input())
data = list(map(int, input().split()))

data.sort()
mid_value = n//2
print(data[mid_value])