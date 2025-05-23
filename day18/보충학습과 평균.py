# 학생 5명의 점수를 알 때 보충을 받을 학생이 모두 보충을 받고 나면 점수의 평균이 몇인지 출력하는 프로그램을 작성하라.

t = int(input())

for test_case in range(1, t+1):
    scores = list(map(int, input().split()))
    total = 0

    for i in range(5):
        if scores[i] < 40:
            scores[i] = 40
        total += scores[i]
    avg = int(total/len(scores))

    print(f"#{test_case} {avg}")