class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa
def sort_students(students_list):  
    sorted_students =sorted (students_list,key=lambda student:student.cgpa,reverse=True)
    return sorted_students
students=[
student("abi","A134",7.8),
student("anu","A135",8.9),
student("hari","A136",9.1),
student("meena","A137",9.9)]
sorted_students=sort_students(students)
for student in sorted_students:
  print("Name:{},RollNumber:{},CGPA:{}".format(student.name, student.roll_number, student.cgpa))

