list_test = [1, 2, 1, 2]
value = 2

while value in list_test:
  list_test.remove(value)

print(list_test) # [1, 1]

import time

number = 0
target_tick = time.time() + 5
while time.time() < target_tick:
  number += 1

print(number)