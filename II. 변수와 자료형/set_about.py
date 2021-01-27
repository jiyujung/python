# 셋 생성
# 형식 : {값 1, 값 2, 값 3, ...}
game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(game)         # {2048, 'LOL', 'Tetris', 1942, 'Overwatch'}
# set(문자열) : 문자열의 문자가 하나씩 셋의 요소로 들어감
print(set("Funny"))     # {'F', 'u', 'y', 'n'}
# set(리스트) : 리스트의 각 요소가 하나씩 셋의 요소로 들어감
print(set([2048, "Tetris", "Cube"]))    # {2048, 'Cube', 'Tetris'}
# set(튜플) : 튜플의 각 요소가 하나씩 셋의 요소로 들어감
print(set((2560, 1440)))    # {2560, 1440}
# set(딕셔너리) : 딕셔너리의 키가 하나씩 셋의 요소로 들어감
print(set({"google":"google.com", 18:"unesco.org"}))    # {'google', 18}
# set(range()) : range() 함수의 각 요소가 하나씩 리스트의 요소로 들어감
print(set(range(3)))    # {0, 1, 2}

# 셋에 추가
# add() : 요소 하나를 추가할 때 사용
game.add("Fifa")
print(game)     # {2048, 1942, 'Tetris', 'Overwatch', 'Fifa', 'LOL'}
# update() : 여러 요소를 추가할 때 사용
game.update(("NBA", "MLB"))
print(game)     # {2048, 'NBA', 1942, 'MLB', 'Tetris', 'Overwatch', 'Fifa', 'LOL'}