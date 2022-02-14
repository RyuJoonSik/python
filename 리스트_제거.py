list_a = [0, 1, 2, 3, 4, 5]

del list_a[1] # 범위 지정 가능
print(list_a) # [0, 2, 3, 4, 5]

list_a.pop(2) # 매개변수를 입력하지 않으면 마지막 요소 제거
print(list_a) # [0, 2, 4, 5]

list_b = [1, 2, 1, 2]
list_b.remove(2) # [1, 1, 2]
print(list_b)

list_c = [0, 1, 2, 3, 4, 5]
list_c.clear()
print(list_c)