# 기본 if 문
# 형식
# if 조건식:       # 조건식이 참이면, 아래 코드 블록 실행
#   명령어1
#   ...
# else:           # 아니면, 아래 코드 블록 실행
#   명령어2
#   ...
x = int(input())        # 입력받아 정수형으로 x에 대입
if x % 2 == 0:          # 변수 x가 2로 나누어 떨어지면
    print("짝수")        # '짝수' 출력
else:                   # 아니면
    print("홀수")        # '홀수' 출력

# input() 함수 : 사용자의 입력을 기다리고, 문자열로 입력받음
password = input()          # 입력받아 password에 대입
if password == "암호":       # 변수 password가 '암호'이면
    # print() 함수 : 화면에 문자열로 출력
    print("암호이다.")        # '암호이다.'를 출력
else:                       # 아니면
    print("암호가 아니다")     # '암호가 아니다.'를 출력

# if ~ elif ~ else 문
# 형식
# if 조건식 1:         # 조건식 1이 참이면, 코드 블록 1을 실행
#   코드 블록 1
# elif 조건식 2:       # 조건식 1이 거짓이고 조건식 2가 참이면, 코드 블록 2를 실행
#   코드 블록 2
# elif 조건식 3:       # 조건식 2가 거짓이고 조건식 3이 참이면, 코드 블록 3을 실행
#   코드 블록 3
# else:               # 전부 아니면, 코드 블록 4를 실행
#   코드 블록 4
x = int(input())
if x % 4 == 0:          # 변수 x가 4로 나누어 떨어지면
    print("4의 배수")    # '4의 배수'를 출력
elif x % 3 == 0:        # 변수 x가 3으로 나누어 떨어지면
    print("3의 배수")    # '3의 배수'를 출력
elif x % 2 == 0:        # 변수 x가 2로 나누어 떨어지면
    print("2의 배수")    # '2의 배수'를 출력

x = int(input())
if 10 <= x < 20:            # 변수 x가 10 이상 20 미만이면
    print("10대")           # '10대'를 출력
elif 30 <= x < 40:          # 변수 x가 30 이상 40 미만이면
    print("30대")           # '30'대를 출력
else:                       # 아니면,
    print("10, 30대가 아님")  # '10, 30대가 아님'을 출력