numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print(r_num) # <list_reverseiterator object at 0x0000013798FEEEC0>
print(next(r_num)) # 6
print(next(r_num)) # 5
print(next(r_num)) # 4
print(next(r_num)) # 3
print(next(r_num)) # 2
print(next(r_num)) # 1