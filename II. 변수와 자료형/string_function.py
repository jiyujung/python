# 문자열을 다루는 다양한 함수
h = "  Happy Programming! "
print(len(h))                       # 글자 수 세기 / 21
print(h.count("p"))                 # h 문자열에서 인자 'p'의 개수 세기 / 2
print(h.upper())                    # 모두 대문자로 변환하기 /   HAPPY PROGRAMMING!
print(h.lower())                    # 모두 소문자로 변환하기 /   happy programming!
print(h.strip())                    # 왼쪽, 오른쪽 모두 공백 없애기 / Happy Programming!
print(h.replace("Happy", "Funny"))  # 문자열 대체하기 /   Funny Programming!
print(h.find("ap"))                 # h 문자열에서 인자 'ap'를 왼쪽부터 찾기 / 3
print(h.rfind("a"))                 # h 문자열에서 인자 'ap'를 오른쪽부터 찾기 / 13
print(h.find("zoo"))                # 찾지 못하면 -1 리턴
print("a" in h)                     # h 문자열에 'a'가 있는지 확인하기 / True
print("amp" in h)                   # h 문자열에 'amp'가 있는지 확인하기 / False
x = "01::23::ab::&&"
y = x.split("::")                   # x 문자열을 '::'로 나누어 리스트 만들기
print(y)                            # ['01', '23', 'ab', '&&']
print(", ".join(y))                 # y 리스트를 ', '로 이어서 문자열 만들기 / 01, 23, ab, &&

# format : 문자열 형식을 미리 정하고, 인자를 주어 문자열을 완성한다.
s = "name: {}, number: {}, soccer: {}"
print(s.format("Ronaldo", 7, True))
print("name: {name}, number: {num}".format(name = "Jordan", num = 23))

# 정수를 표현하는 여러 가지 방법
print("{:d}".format(515))           # 정수를 넣는다 / 515
print("{:5d}".format(515))          # 최소 5칸을 차지하고 정수를 넣는다 /   515
print("{:+5d}".format(515))         # 양수면 +를 표시한다 /  +515
print("{:=+5d}".format(515))        # +를 맨 앞에 표시한다 / + 515
print("{:05d}".format(515))         # 빈칸은 0으로 채운다 / 00515
print("{:+05d}".format(515))        # 양수면 0 앞에 +를 표시한다 / +0515