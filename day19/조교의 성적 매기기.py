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
    group_index = (rank-1) // group_size

    print(f"#{test_case} {grade[group_index]}")