# 입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고, 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때, K 번째 학생의 학점을 출력하는 프로그램을 작성하라.

t = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']


for test_case in range(1, t+1):
    n, k = map(int, input().split())
    score = []

    for _ in range(n):
        a, b, c = map(int, input().split())
        total_score = a*0.35 + b*0.45 + c*0.2
        score.append(total_score)

    target_score = score[k-1]
    score.sort(reverse=True)

    rank = score.index(target_score) + 1

    group_size = n//10
    # 전체 학생 수 n을 10으로 나눠서 한 학점을 받을 인원 수를 계산
    group_index = (rank-1) // group_size
    # 순위를 통해 어떤 학점 그룹에 속하는지 계산

    print(f"#{test_case} {grade[group_index]}")