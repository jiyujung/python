# 기본적인 while 문
# 형식
# while 조건식:       # 조건식을 만족하면, 코드 블록을 반복
#   코드 블록         # 무한 반복이 되지 않게 주의

# x = 3
# while x < 6:
#     print(x)      # 3을 무한 반복

x = 3
while x < 6:
    print(x)
    x += 1          # x를 1씩 증가

echo = input()
while echo != "exit":       # 변수가 exit가 아니면 코드 블록을 실행
    print(echo)
    echo = input()          # 새로 입력을 받아 변수를 바꿈

echo = input()
while True:                 # 코드 블록을 무한 반복
    if echo == "exit":
        break               # 조건문을 만족하면 반복문을 멈춤
    print(echo)
    echo = input()          # 새로 입력을 받아 변수를 바꿈