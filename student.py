def get_average_score(name , students):
    for student in students:
        if student["name"] == name:
            scores = student["scores"].values()
            return sum(scores)  / len(scores)
# print(get_average_score("Charlie" , students))
def find_top_students(students):
    for student in students:
        top_score =0
        top_student =""
        # avg_score = sum(student["scores"].values())/(len(student["scores"]))

def failed_students(students , passing_score=50)
   for student in students:
    grades = student.get("grade", {})
   if  any(student score < passing_score for
    score in grades.values()):
    failed_list.append(student["name"])
    return failed_list
    students [
        {"name":"Samir", "grade" , [57 , 65 , 80]}
        {"name":"Asan", "grade", [47 , 61 , 79]}
        {"name":"Nuri", "grade", [58 , 70 ,81]}
    ]
#    print(failed_students(students , passing_score=50))

class student:
    def __init__(self , name , student_id , grades):
      self.name = name
      self.student_id = student_id
      self.grades = grades
    def add_grade(self , grade):
      self.grades.append(grade)
    def calculate_average(self):
        average = sum(self.grades) / len(self.grades)
        return average

        def display_info(self):
            print(f"student:{self.name}, Student id:{self.student_id},Grade: {self.grades}")
      std = Student("Alice" ,101 )
      std.add_grade(88)
      std.add_grade(92)
      std.add_grade(100)
    #   std.display_info()     
class student:
    def ___init__(self , name , student_id , grades):
        self.name = name
        self.student_id = student_id
        self. grades = grades
    def add_grade(self ,grade):
        self.grades.append(grade)
    def calculate_average(self):
        return sum(self.grades)
        

