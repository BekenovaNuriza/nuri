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
   print(failed_students(students , passing_score=50))
