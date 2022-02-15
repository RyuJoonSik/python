# try:
#   number_input_a = int(input())

#   print(number_input_a)
# except:
#   print("정수가 아닌 값")

# list_input_a = ["52", "274", "32", "스파이", "103"]
# list_number = []

# for item in list_input_a:
#   try:
#     float(item)
#     list_number.append(item)
#   except:
#     pass

# print("{}".format(list_number)) # ['52', '274', '32', '103']

# try:
#   number_input_a = int(input())
# except:
#   print("정수를 입력하지 않음")
# else:
#   print(number_input_a)

# try:
#   number_input_a = int(input())
#   print(number_input_a)
# except:
#   print("정수를 입력하지 않음")
# else:
#   print("예외가 발생하지 않음")
# finally:
#   print("프로그램 종료")

def test():
  print("test 함수 첫 줄")
  
  try:
    print("try 구문 실행")
    return
    print("try 구문의 return 뒤 구문")
  except:
    print("except 구문 실행")
  else:
    print("else 구문 실행")
  finally:
    print("finally 구문 실행")
  print("test() 함수의 마지막 줄")

test()

# test 함수 첫 줄
# try 구문 실행
# finally 구문 실행

print("프로그램 실행")

while True:
  try:
    print("try 구문 실행")
    break
    print("try 구문 break 키워드 뒤")
  except:
    print("except 구문의 실행")
  finally:
    print("finally 구문 실행")
  print("while 반복문의 마지막 줄")
print("프로그램 종료")