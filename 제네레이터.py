def test():
  print("A")
  yield 1
  print("B")
  yield 2
  print("C")
  yield 3

output = test() # 제네레이터 반환
a = next(output)
print(a) # 1

b = next(output)
print(b) # 2

c = next(output)
print(c) # 3

a, b = int(input()), int(input())
print(a + b)