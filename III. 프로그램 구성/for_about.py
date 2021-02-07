# 기본적인 for문
# 형식 : for 변수 in range() 함수:
for x in range(3, 9, 2):            # 3부터 (9-1)까지 2씩 증가하는 수
    print(x)
# 형식 : for 변수 in 문자열:
for ch in "LOVE":
    print(ch)
# 형식 : for 변수 in  리스트:
for item in ["힙합", "발라드"]:
    print(item + " 즐겨 듣는다.")
# 형식 : for 변수 in 튜플:
for item in (2560, 1440):
    print(item)
# 형식 : for 변수 in 딕셔너리:
pl = {"C":1972, "Java":1995, "Python":1991}
for key in pl:
    print(key, ":", pl[key])
# 형식 : for 변수 in 셋:
for item in {"HTML5", "CSS3", "JavaScript"}:
    print(item + "를 할 수 있다.")

# 중첩 반복문
for i in range(1, 9+1):
    print("2 x {} = {}".format(i, 2*i))     # 구구단 2단을 출력
for i in range(1, 9+1):
    print("3 x {} = {}".format(i, 3*i))     # 구구단 3단을 출력
for i in range(1, 9+1):
    print("4 x {} = {}".format(i, 4*i))     # 구구단 4단을 출력
for i in range(1, 9+1):
    print("5 x {} = {}".format(i, 5*i))     # 구구단 5단을 출력
# 구구단 2~5단을 출력
for dan in range(2, 5+1):
    for i in range(1, 9+1):
        print("{} x {} = {}".format(dan, i, dan*i))
    print('---------------')
table = [["월", "화", "수"], [100, 200, 300]]
for row in table:
    for col in row:
        print(str(col)+" ")
    print()