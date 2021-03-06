# 하나의 값을 리턴하는 함수
def sum(*numbers):
    sum_value = 0
    for number in numbers:
        sum_value = sum_value + number
    return sum_value
result = sum(1, 3)
print("1 + 3 = ", result)
print("1 + 3 + 5 + 7 = ", sum(1, 3, 5, 7))

def min(*numbers):
    min_value = numbers[0]
    for number in numbers:
        if min_value < number:
            min_value = number
    return min_value
result = min(1, 3)
print("min(1, 3) = ", result)
print("min(0, 3, -11) = ", min(0, 3, -11))

# 리스트를 사용해 여러 값을 하나로 묶어 리턴하기
def multi_num(multi, start, end):
    result = []
    for n in range(start, end):
        if n % multi == 0:
            result.append(n)
    return result
multi2 = multi_num(17, 1, 200)
print("multi_num(17, 1, 200) : ", multi2)
print()
multi3 = multi_num(3, 1, 100)
print("multi_num(3, 1, 100) : ", multi3)

# 튜플을 사용해 여러 값을 여러 개 리턴하기
def min_max(*args):
    min = args[0]
    max = args[0]
    for arg in args:
        if min > arg:
            min = arg
        if max < arg:
            max = arg
    return min, max
print(min_max(52, -3, 23, 89, -21))
min_value, max_value = min_max(52, -3, 23, 89, -21)
print("최저값:", min_value)
print("최고값:", max_value)