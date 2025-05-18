n = int(input())

for i in range(1, n+1):
    count = 0
    for digit in str(i):
        if digit in "369":
            count += 1
    
    if count > 0:
        print("-"*count, end=" ")
    else:
        print(i, end=" ")