# N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(m):
        first = arr.pop(0)
        arr.append(first)

    print("#"+str(test_case), arr[0])

# for test_case in range(t+1):
#     n, m = map(int, input().split())
#     for _ in range(n):
#         arr = int(input())
#     for i in range(len(arr)):
#         arr[i] = arr[i+1]
#         arr[i+1] = arr[i+2]
#         arr[len(arr)-1] = arr[i]
#     print(arr[len(arr)-1])


