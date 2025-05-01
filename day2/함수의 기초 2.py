# 사용자 2명으로부터 가위, 바위, 보를 입력 받아 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.

def who_is_winner(choice1, choice2):
    if (choice1 == choice2) :
        return "비겼습니다!"
    elif (choice1 == "가위" and choice2 == "보") or (choice1 == "바위" and choice2 == "가위") or (choice1 == "보" and choice2 == "바위"):
        return f"{choice1}가 이겼습니다!"
    else:
        return f"{choice2}가 이겼습니다!"
    
name1 = input()
name2 = input()
choice1 = input()
choice2 = input()

print(who_is_winner(choice1, choice2))