print ("STUDENT MARK MANAGEMENT")
print ("")

# Input number of students in a class
def numOfStudents ():
    return int(input("How many students are there in this class?: "))
#-----------------------------------------
# Input student information: id, name, DoB
print ("STUDENT INFORMATION")
inforS = numOfStudents ()
listOfStudents = []   
for i in range (inforS): 
    Student_ID = input ("ID: ")
    Student_Name = input ("Name: ")
    Student_DoB = input ("DoB (mm/dd/yyyy): ")
    print ("")
    inforS = {"Student_ID: ": Student_ID, 
              "Student_Name: ": Student_Name, 
              "Student_DoB: ": Student_DoB}
    listOfStudents.append (Student(Student_ID, Student_Name, Student_DoB))
    
def numOfCourses ():
    return int(input ("How many courses are there in this class?: "))
#-----------------------------------------
# Input course information: id, name
print ("")
print ("COURSE INFORMATION")

inforC = numOfCourses ()
listOfCourses = []
for i in range (inforC):
    Course_ID = input ("ID: ")
    Course_Name = input ("Name: ")
    Course_Credits = input ("Credit(s): ")
    print ("") 
    inforC = {"ID": Course_ID,
              "Name": Course_Name,
              "Credit(s)": Course_Credits}
    listOfCourses.append (Course(Course_ID, Course_Name, Course_Credits))
    
# Select a course, input marks for student in this course
print ("")
print ("SELECT A COURSE, INPUT MARKS FOR STUDENTS IN THIS COURSE")

StudentMark = []
selectCourse = 0
while selectCourse in range (0, len(listOfCourses), 1):
    selectCourse = int(input("Select a course: "))
    if selectCourse > len(listOfCourses):
        break
    for i in range (0, len(listOfStudents), 1):
        print (f"Course {selectCourse} - input mark for student {Student_ID[0]}: ")
        mark = int(input())
        StudentMark.append({Student_ID[0]: mark})