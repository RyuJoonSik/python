a = range(5)
print(a) # range(0, 5)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 5))) # [0, 1, 2, 3, 4]
print(list(range(5, 10))) # [5, 6, 7, 8, 9]
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]
print(list(range(0, 10, 3))) # [0, 3, 6, 9]

for i in range(5):
  print(i)

for i in range(5, 10):
  print(i)

for i in range(0, 10, 3):
  print(i)

array = [273, 32, 103, 57, 52]

for i in range(len(array)):
  print(array[i])

for i in range(4, -1, -1):
  print(i)

for i in reversed(range(5)):
  print(i)