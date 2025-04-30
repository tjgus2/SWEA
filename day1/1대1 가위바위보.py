#A와 B가 가위바위보를 하였다 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다. A와 B중에 누가 이겼는지 판별해보자

n, m = map(int, input().split())

if (n==1 and m==2) or (n==2 and m==1):
    print("B")
elif (n==1 and m==3) or (n==3 or m==1):
    print("A")
elif (n==2 and m==3) or (n==3 or m==2):
    print("B")