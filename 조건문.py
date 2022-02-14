number = input("정수 입력>")
number = int(number)

if number > 0:
  print("양수")

if number < 0:
  print("음수")

if number == 0:
  print("0");

number_1 = input("정수 입력>")
number_1 = int(number)

if number % 2 == 0:
  print("짝수")
else:
  print("음수")

import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
  print("봄")
elif 6 <= month <= 8:
  print("여름")
elif 9 <= month <= 11:
  print("가을")
else:
  print("겨울")
