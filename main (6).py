class Student:
    def_init_(self,name,roll_number,cgpa):
    self.name=name
  self.roll_number=roll_number
  self.cpga=cgpa

def sort_student(student_list):

#Sort the list of student in descending order of CGPA

sorted_student=sorted(student_list,key=lambdastudent:student.cpga,
reverse=True)

return sorted_students
#Example usage:

students=[
  Student("Harini","A123",7.8),
  Student("Sri","A124",8.9),
  Student("Yasica","A125",9.1),
  Student("Priya","A126",9.9),
]

sorted_students=sort_students(students)
#print the sorted list of students
for student in sorted_students:

  print("Name:{},Roll Number:{},CGPA:{}",format(student_name,student.roll_number,student.cgpa))
