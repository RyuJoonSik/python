dict_a = {
  "name": "어벤저스 엔드게임",
  "type": "히어로 무비"
}

print(dict_a["name"]) # 어벤저스 엔드게임
print(dict_a["type"]) # 히어로 무비

name = "이름"
dict_key = {
  name: "7D 건조 망고",
  type: "당절임"
}

print(dict_key) # {'이름': '7D 건조 망고', <class 'type'>: '당절임'}

dictionary = {
  "name": "7D 건조 망고",
  "type": "당절임",
  "ingredients": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
  "origin": "필리핀"
}

print("name" in dictionary) # True
print("nam" in dictionary) # False

print(dictionary.get("name")) # 7D 건조 망고
print(dictionary.get("nam")) # None

for key in dictionary:
  print("{}, ".format(dictionary[key]), end='')