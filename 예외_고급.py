# try:
#   number_input_a = int(input())

#   print(number_input_a)
# except Exception as exception:
#   print("정수를 입력하지 않음")
#   print(type(exception), exception) # <class 'ValueError'> invalid literal for int() with base 10: 'yes'

# list_number = [52, 273, 32, 72, 100]

# try:
#   number_input = int(input())

#   print("{} {}".format(number_input, list_number[number_input]))
# except ValueError:
#   print("정수를 입력하지 않음")
# except IndexError:
#   print("리스트의 인덱스를 벗어남")

# try:
#   number_input = int(input())
  
#   print("{} {}".format(number_input, list_number[number_input]))
# except ValueError as exception:
#   print("정수를 입력하지 않음")
#   print(exception)
# except IndexError as exception:
#   print("리스트의 인덱스를 벗어남")
#   print(exception)


# list_number = [52, 273, 32, 72, 100]

# try:
#   number_input = int(input())

#   print("{} {}".format(number_input, list_number[number_input]))
#   예외.발생()
# except ValueError as exception:
#   print("정수를 입력하지 않음")
#   print(type(exception), exception)
# except IndexError as exception:
#   print("리스트의 인덱스를 벗어남")
#   print(type(exception), exception)
# except Exception as exception:
#   print("예상치 못한 에러 발생")
#   print(type(exception), exception)

number = int(input())

if number > 0:
  raise NotImplementedError
else:
  raise NotImplementedError
