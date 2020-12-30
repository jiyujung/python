# 슬라이싱 : 문자열에서 원하는 부분을 잘라서 가져온다.
# 형식 : 문자열[인덱스1:인덱스2]
s = "Life is too short, You need Python."
print(s[3:7])       # 인덱스 3번부터 인덱스 7번 바로 앞까지 / e is
print(s[-10:-7])    # 인덱스 -10번부터 인덱스 -7번 바로 앞까지 / ed
print(s[3:-10])     # 인덱스 3번부터 인덱스 -10번 바로 앞까지 / e is too short, You ne
print(s[-10:30])    # 인덱스 -10번부터 인덱스 30번 바로 앞까지 / ed Py
print(s[3:2])       # 인덱스 3번부터 인덱스 2번 바로 앞까지 / 못 구함
print(s[30:])       # 인덱스 30번부터 맨 뒤까지 / thon.
print(s[-7:])       # 인덱스 -7번부터 맨 뒤까지 / Python.
print(s[:4])        # 맨 앞부터 인덱스 4번 바로 앞까지 / Life
print(s[:-17])      # 맨 앞부터 인덱스 17번 바로 앞까지 / Life is too short,
print(s[:])         # 맨 앞부터 맨 뒤까지. 즉 문자열 전체 / Life is too short, You need Python.