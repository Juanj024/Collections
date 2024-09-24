#Asking for inputs
studentName = input("Introduce the name of the student  ")

grade1 = int(input("Introduce your first grade  "))
grade2 = int(input("Introduce your second grade  "))
grade3 = int(input("Introduce your third grade  "))
grade4 = int(input("Introduce your fourth grade  "))
grade5 = int(input("Introduce your fifth grade  "))

#Creating function
def letterGrade(grade1,grade2,grade3,grade4,grade5):
    average = (grade1 + grade2 + grade3 + grade4 + grade5 ) / 5
    print ("Average:","%.1f" % average )
    # now the representation of the grade on one letter
    if average <= 100 and average >= 90:
        print ("Letter Grade: A")
    elif average < 90 and average >=80:
        print ("Letter Grade: B")
    elif average < 80 and average >= 70:
        print ("Letter Grade: C")
    elif average < 70 and average >= 60:
        print ("Letter Grade: D")
    elif average < 60 and average >= 0:
        print ("Letter Grade: F")
    else:
        print ("No computable grades !!!!")

print()
print()
print (studentName)
letterGrade(grade1,grade2,grade3,grade4,grade5)