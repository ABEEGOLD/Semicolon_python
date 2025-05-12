number_of_students = int(input("Enter number of students: "))
largest = 0
student_score = 0
name_Of_Student = ""

 
for number in range(number_of_students):
	student_Name = input("student name: ")
	student_Score =int(input("Enter score of student: "))


	if student_Score > largest:
		largest = student_Score
		name_Of_Student = student_Name
print(f"Student {name_Of_Student} largest score is: {largest} ")
	



 

