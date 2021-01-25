# 딕셔너리 생성
# 형식 : {키 1 : 값 1, 키 2 : 값 2, 키 3 : 값 3, ...}
d = {}      # 빈 딕셔너리
urls = {"google" : "google.com", "18" : "unesco.org"}

# 딕셔너리에 요소 추가
urls["x"] = 2560        # 키 'x'가 딕셔너리에 없으면, 추가
print(urls)

# 딕셔너리에 요소 수정
urls["x"] = 1920        # 키 'x'가 딕셔너리에 있으면, 수정
print(urls)

# 딕셔너리에 요소 제거
del urls["x"]                # {"google" : "google.com", "18" : "unesco.org"}
print(urls.pop("18"))        # {"google" : "google.com"} / unesco.org
print(urls.clear())          # {}

# 딕셔너리에서 요소 검색
urls = {"google" : "google.com", "18" : "unesco.org"}
print(urls["google"])                   # 키 'google'의 값을 가져옴 / google.com
print(urls.get("google"))               # 키 'google'의 값을 가져옴 / google.com
# 키 in 딕셔너리 : 딕셔너리에 키가 있는지 확인
print("google" in urls)                 # 키 'google'이 있는지 확인 / True
print("google.com" in urls)             # 키 'google.com'이 있는지 확인 / False
# 키 in 딕셔너리.values() : 딕셔너리에 값이 있는지 확인
print("google.com" in urls.values())    # True

# 기타 딕셔너리 관련 함수
print(len(urls))        # 2
# 딕셔너리.keys() : 딕셔너리의 키들을 dict_keys 객체로 리턴
print(urls.keys())      # dict_keys(['google', '18'])
# 딕셔너리.values() : 딕셔너리의 값들을 dict_values 객체로 리턴
print(urls.values())    # dict_values(['google.com', 'unesco.org'])
# 딕셔너리.items() : 딕셔너리의 키와 값의 쌍을 묶어 dict_items 객체로 리턴
print(urls.items())     # dict_items([('google', 'google.com'), ('18', 'unesco.org')])