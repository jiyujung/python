# 튜플 생성
# 형식 : (값 1, 값 2, 값 3, ...)
t = ()                  # 빈 튜플
xy = (2560, 1440)       # (2560, 1440)
color = 129, 247, 216   # (129, 247, 216)
xy + color              # (2560, 1440, 129, 247, 216)
xy * 2                  # (2560, 1440, 2560, 1440)

# 패킹과 언패킹
color = 129, 247, 216       # 패킹(129, 247, 216)
red, green, blue = color    # 언패킹
print(red)      # 129
print(green)    # 247
print(blue)     # 216
x, y = 1920, 1080
print(x)        # 1920
print(y)        # 1080

# 튜플 활용
x = 2560
y = 1440
x, y = y, x      # 직관적인 교환(swap)이 가능
print(x)        # 1440
print(y)        # 2560
a = (123, "abc", True, 123)
print(a[1])     # 인덱싱 / abc
print(a[2:])    # 슬라이싱 / (True, 123)
print(a[:2])    # (123, 'abc')
# a[1] = 2      # 튜플은 값을 수정할 수 없음
# index(값) : 값에 해당하는 인덱스를 가져옴
print(a.index("abc"))   # 1
# count(값) : 값에 해당하는 요소의 개수를 가져옴
print(a.count(123))     # 2