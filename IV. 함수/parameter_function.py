# 매개 변수가 하나인 함수
import random
# 인자 값 - 주사위 눈 수 조정. pip : 주사위의 눈을 의미
def rolling_dice(pip):
    n = random.randint(1, pip)
    print(pip, "면 주사위 굴린 결과 : ", n)
rolling_dice(4)
rolling_dice(6)
rolling_dice(6)
rolling_dice(8)
rolling_dice(10)
rolling_dice(12)
rolling_dice(20)

# 매개 변수가 여러 개인 함수
# 인자 값 - 주사위 여러 번 굴리게 함
def rolling_dice(pip, repeat):
    for r in range(1, repeat + 1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린 결과", r, " : ", n)
rolling_dice(6, 1)
rolling_dice(6, 2)
rolling_dice(12, 0)
rolling_dice(20, -3)

# 매개 변수에 가변 인수가 있는 함수
print("♡")
print("♡", "♪")
print("♡", "♪", "♣")
print("♡", "♪", "♣", "♠")
print("♡", "♪", "♣", "♠", "★")
def p(*args):
    str = ""
    for a in args:
        str = str + a
    print(str)
p("♡")
p("♡", "♪")
p("♡", "♪", "♣", "♠")
def p(space, space_num, *args):
    str = args[0]
    for i in range(1, len(args)):
        str = str + (space * space_num) + args[i]
    print(str)
p(",", 3, "♡", "♪")
p("☆", 2, "♡", "♪", "♣")
p("_", 3, "♡", "♪", "♣", "♠")