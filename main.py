#Asking for inputs
studentName = input("Introduce the name of the student  ")

grade = [int(input("Introduce first grade ")), int(input("Introduce second grade ")), int(input("Introduce third grade ")), int(input("Introduce fourth grade ")), int(input("Introduce fifth grade "))]

#Creating function
def letterGrade(grade):
	average = (grade[0] + grade[1] + grade[2] + grade[3] + grade[4]) / (len(grade))
	print("Average:", "%.1f" % average)
#now the representation of the grade on one letter
	if average <= 100 and average >= 90:
		print("Letter Grade: A")
	elif average < 90 and average >= 80:
		print("Letter Grade: B")
	elif average < 80 and average >= 70:
		print("Letter Grade: C")
	elif average < 70 and average >= 60:
		print("Letter Grade: D")
	elif average < 60 and average >= 0:
		print("Letter Grade: F")
	else:
		print("No computable grades !!!!")

print()
print(studentName)

letterGrade(grade)