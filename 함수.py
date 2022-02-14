def print_n_times(n, *values):
  for i in range(n):
    for value in values:
      print(value)

print_n_times(3, "안녕하세요", "즐거운", "파이썬")

def print_n_times(value, n=2):
  for i in range(n):
      print(value)

print_n_times("안녕하세요")

def print_n_times(*values, n=2):
  for i in range(n):
    for value in values:
      print(value)

print_n_times("안녕하세요", "즐거운", "파이썬", n = 3)

[a, b] = [10, 20]
(c, d) = (10, 20)

print(a) # 10
print(b) # 20
print(c) # 10
print(d) # 20

tuple_test = 10, 20, 30, 40
print(tuple_test, type(tuple_test)) # (10, 20, 30, 40) <class 'tuple'>

e, f, g = 10, 20, 30
print(e, f, g) # 10 20 30

h, i = 10 , 20
print(h, i) # 10 20

h, i = i, h
print(h, i) # 20 10

def test():
  return (10, 20)

a, b = test()
print(a) # 10
print(b) # 20

def call_10_times(func):
  for i in range(10):
    func()

def print_hello():
  print("hello")

call_10_times(print_hello)

def power(item):
  return item * item

def under_3(item):
  return item < 3

power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x: x * x, list_input_a)
print(output_a) # <map object at 0x0000019C265E3D90>
print(list(output_a)) # [1, 4, 9, 16, 25]

output_b = filter(lambda x: x < 3, list_input_a)
print(output_b) # <filter object at 0x0000019C265E3D30>
print(list(output_b)) # [1, 2]