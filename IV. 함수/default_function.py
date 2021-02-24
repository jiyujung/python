# 기본 인자 값을 가지는 함수
def hello(msg="안녕하세요"):
    print(msg + "!")
hello("오랫만이에요")
hello("이영희")
hello()
def hello(name="무명", msg="안녕하세요"):
    print(name + "님, " + msg + "!")
hello("김철수", "오랫만이에요")
hello()
def hello(name, msg="안녕하세요"):
    print(name + "님, " + msg + "!")
hello("김철수", "오랫만이에요")
hello("이영희")

# 기본 인자 값이 가변 객체인 함수
def fn(a, b=[]):
    b.append(a)
    print(b)
fn(3)
fn(5)
fn(10)