import csv

print("Grade manager")

class Students:
    def __init__(self, name, course, score):
        self.name = name 
        self.course = course
        self.score = score
  
Student_list = []

add_students ='yes'

def separate_score(student):
    return student.score

while add_students == 'yes':
    name = input("Enter student's initials: ")
    course = input("What is the course code?: ")
    score = float(input("Student's score: "))

    student = Students(name, course, score)

    Student_list.append(student)

    while True:
         add_students = input("Do you wish to continue? ").strip().lower()
         if add_students == 'yes' or add_students == 'no':
              break
         else:
             print("Invalid input, enter yes or no")

Student_list.sort(key = separate_score, reverse = True)

for student in Student_list:
    print([student.name, student.course, student.score])

with open('SGM.csv', mode = 'w', newline = "") as file:
     writer = csv.writer(file)

     writer.writerow(['Name', 'Course', 'Score', 'Rank'])

     rank = 1

     for student in Student_list:
          writer.writerow([student.name, student.course, student.score, rank])
          rank = rank + 1