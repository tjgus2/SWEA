# 문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다. 반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.

t = int(input())

for test_case in range(1, t+1):
    s = input()
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            # 스택이 비어 있지 않고 방금 넣은 문자와 지금 문자와 같다면
            stack.pop()
            # 스택에서 제거
        else:
            stack.append(ch)
            # 현재 문자를 스택에 추가

    print("#"+str(test_case), len(stack))