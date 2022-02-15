class Student:
  count = 0
  students = []

  @classmethod
  def print(cls):
    for student in cls.students:
      print(str(student))

  def __init__(self, name, korean, math, english, science):
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science
    Student.count += 1
    Student.students.append(self)

  def get_sum(self):
    return self.korean + self.math + self.english + self.science
  
  def get_average(self):
    return self.get_sum() / 4

  def __str__(self):
    return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

Student("A", 87, 98, 88, 95)
Student("B", 92, 98, 96, 98)

Student.print()