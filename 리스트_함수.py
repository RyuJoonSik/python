temp = [1, 2, 3, 4, 5]

# for i in temp:
#   print(i)

# for i in temp:
#   print(i)

for i in reversed(temp):
  print(i)

for i in reversed(temp):
  print(i)

print(temp[::-1])

example_list = ["요소A", "요소B", "요소C"]

print(enumerate(example_list)) # <enumerate object at 0x00000211FAFA3FC0>
print(list(enumerate(example_list))) # [(0, '요소A'), (1, '요소B'), (2, '요소C')]

for i, value in enumerate(example_list):
  print(i, value) # 0 요소A, 1 요소B, 2 요소C

array = []

for i in range(0, 20, 2):
  array.append(i * i)

print(array) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 리스트 내포
array = [i * i for i in range(0, 20, 2)]
print(array)

array_1 = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array_1 if fruit != "초콜릿"]

print(output)