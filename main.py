def grades_average(grades):
  grades_count = 0
  grades_sum = 0
  for course in grades:
      grades_count += len(grades[course])
      grades_sum += sum(grades[course])
  return round(grades_sum / grades_count, 1)


class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades_student = {}
      self.grades_average_homework = []

  def rate_hw_lecturer(self, lecturer, course, grade):
      if isinstance(lecturer,
                    Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
          if course in lecturer.grades_lecturer:
              lecturer.grades_lecturer[course] += [grade]
          else:
              lecturer.grades_lecturer[course] = [grade]
      else:
          return 'Ошибка'

  def grades_average(self):
      grades_count = 0
      grades_sum = 0
      for grade in self.grades_student:
          grades_count += len(self.grades_student[grade])
          grades_sum += sum(self.grades_student[grade])
      return grades_sum / grades_count

  def __str__(self):
      return (f"Имя: {self.name}\n"
              f"Фамилия: {self.surname}\n"
              f"Средняя оценка за домашние задания: {grades_average(self.grades_student)}\n"
              f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
              f"Завершенные курсы: {', '.join(self.finished_courses)}\n")


class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []
      self.grades_lecturer = {}


class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.courses_attached = []
      self.grades_lecturer = {}
      self.grades_average_lecture = []

  def __str__(self):
      return (f"Имя: {self.name}\n"
              f"Фамилия: {self.surname}\n"
              f"Средняя оценка за лекции: {grades_average(self.grades_lecturer)}\n")


class Reviewer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)

  def rate_hw_student(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades_student:
              student.grades_student[course] += [grade]
          else:
              student.grades_student[course] = [grade]
      else:
          return 'Ошибка'

  def __str__(self):
      return (f"Имя: {self.name}\n"
              f"Фамилия: {self.surname}\n")


def average_hw_grade_by_course(students, course):
  total_grades = 0
  students_count = 0

  for student in students:
      if course in student.grades_student:
          total_grades += sum(student.grades_student[course])
          students_count += len(student.grades_student[course])

  if students_count == 0:
      return 0

  return round(total_grades / students_count, 1)


def average_lecture_grade_by_course(lecturers, course):
  total_grades = 0
  lecturers_count = 0

  for lecturer in lecturers:
      if course in lecturer.grades_lecturer:
          total_grades += sum(lecturer.grades_lecturer[course])
          lecturers_count += len(lecturer.grades_lecturer[course])

  if lecturers_count == 0:
      return 0

  return round(total_grades / lecturers_count, 1)

########

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student_2 = Student('Ruoy2', 'Eman2', 'your_gender')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Git']
best_student_2.finished_courses += ['Введение в программирование']

########

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

cool_mentor_2 = Reviewer('Some2', 'Buddy2')
cool_mentor_2.courses_attached += ['Python']
cool_mentor_2.courses_attached += ['Git']

########

awesome_lecturer = Lecturer('Another', 'Lecturer')
awesome_lecturer.courses_attached += ['Python']

awesome_lecturer_2 = Lecturer('Another2', 'Lecturer2')
awesome_lecturer_2.courses_attached += ['Python']

########

cool_mentor.rate_hw_student(best_student, 'Python', 8)
cool_mentor.rate_hw_student(best_student, 'Python', 7)
cool_mentor.rate_hw_student(best_student, 'Python', 9)
cool_mentor.rate_hw_student(best_student, 'Git', 10)

cool_mentor_2.rate_hw_student(best_student_2, 'Python', 7)
cool_mentor_2.rate_hw_student(best_student_2, 'Python', 6)
cool_mentor_2.rate_hw_student(best_student_2, 'Python', 8)
cool_mentor_2.rate_hw_student(best_student_2, 'Git', 9)

########

best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 8)
best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 9)
best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 10)

best_student_2.rate_hw_lecturer(awesome_lecturer_2, 'Python', 6)
best_student_2.rate_hw_lecturer(awesome_lecturer_2, 'Python', 8)
best_student_2.rate_hw_lecturer(awesome_lecturer_2, 'Python', 9)

########
average_hw_grade = average_hw_grade_by_course([best_student, best_student_2], 'Python')
average_lecture_grade = average_lecture_grade_by_course([awesome_lecturer, awesome_lecturer_2], 'Python')

print('########')
print(cool_mentor)
print(awesome_lecturer)
print(best_student)

print('########')
print(cool_mentor_2)
print(awesome_lecturer_2)
print(best_student_2)
print('########')

print(f"Средняя оценка за домашние задания по курсу Python: {average_hw_grade}")
print(f"Средняя оценка за лекции по курсу Python: {average_lecture_grade}")