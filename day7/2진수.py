# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

t = int(input())

for test_case in range(1, t+1):
    N, hex_str = input().split()

    result = ""
    for ch in hex_str:
        binary_digit = bin(int(ch, 16))[2:].zfill(4)
        result += binary_digit

    print("#"+str(test_case), result)