t = int(input())

for test_case in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())

    h_reuslt = h1 + h2
    m_result = m1 + m2
    
    if m_result >= 60:
        m_result -= 60
        h_reuslt += 1

    if h_reuslt > 12:
        h_reuslt -= 12

    print(f"#{test_case} {h_reuslt} {m_result}")
        
    