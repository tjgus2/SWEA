#해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 ”YYYY/MM/DD”형식으로 출력하고, 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

t = int(input())

for test_case in range(1, t+1):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date = input()
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])

    result = date[0:4] + "/" + date[4:6] + "/" + date[6:8]

    if 0<month<13 and 0<day<=days[month-1]:
        print("#"+str(test_case), result)
    else:
        print("#"+str(test_case), -1)