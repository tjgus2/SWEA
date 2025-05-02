# N=2^a x 3^b x 5^c x 7^d x 11^e 
# N이 주어질 때 a, b, c, d, e 를 출력하라.

t = int(input())

for test_case in range(1, t+1):

    n = int(input())
    a = b = c = d  = e = 0
    
    while n % 2 == 0:
        a += 1
        n //= 2
        
    while n % 3 == 0:
        b += 1
        n //= 3

    while n % 5 == 0:
        c += 1
        n //= 5

    while n % 7 == 0:
        d += 1
        n //= 7

    while n % 11 == 0:
        e += 1
        n //= 11
    
    print("#"+str(test_case), a, b, c, d, e)


        # if n % 2 == 0:
        #     a += 1
        # elif n % 3 == 0:
        #     b += 1
        # elif n % 5 == 0:
        #     c += 1
        # elif n % 7 == 0:
        #     d += 1
        # elif n % 11 == 0:
        #     e += 1