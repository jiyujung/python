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