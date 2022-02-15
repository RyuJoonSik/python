class Parent:
  def __init__(self):
    self.value = "테스트"
    print("Parent 클래스 __init()__ 호출")
  def test(self):
    print("Parent 클래스 test() 메소드")

class Child(Parent):
  def __init__(self):
    Parent.__init__(self)
    print("Child 클래스 __init()__ 호출")

child = Child()
child.test()
print(child.value)

class CustomException(Exception):
  def __init__(self, message, value):
    Exception.__init__(self)
    self.message = message
    self.value = value

  def __str__(self):
    return self.message

  def print(self):
    print("오류 정보")
    print(self.message)
    print(self.value)

try:
  raise CustomException("오류 발생", 200)
except CustomException as e:
  e.print()