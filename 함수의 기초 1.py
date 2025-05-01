# 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고 그 함수를 이용해 회문 여부를 판단하는 코드를 작성하십시오.

def reverse_string(word):
    return word[::-1]

def is_palindrome(word):
    reversed_word = reverse_string(word)
    return word == reversed_word

word = input("단어를 입력하세요: ")

if is_palindrome(word):
    print(word)
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print(word)