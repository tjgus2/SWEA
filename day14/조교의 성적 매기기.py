t = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    # n: 학생수 k: 학점을 알고싶은 학생의 번호
    score = []

    for _ in range(n):
        a, b, c = map(int, input().split())
        total_grade = 0.35*a + 0.45*b + 0.2*c

        score.append(total_grade)

    target_score = score[k-1]
    sorted_score = sorted(score, reverse=True)

    rank = sorted_score.index(target_score)

    group_size = n//10
    group_index = rank // group_size

    print(f"#{test_case} {grade[group_index]}")