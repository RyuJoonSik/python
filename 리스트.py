list_a = [1, 2, 3]
list_b = [4, 5, 6]

print(list_a) # [1, 2, 3]
print(list_b) # [4, 5, 6]
print(list_a + list_b) # [1, 2, 3, 4, 5, 6]
print(list_a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(list_a)) # 3

list_c = [1, 2, 3]
list_c.append(4)
print(list_c) # [1, 2, 3, 4]

list_c.insert(0, 10) # [10, 1, 2, 3, 4]
print(list_c)

list_c.extend([5, 6, 7])
print(list_c)
