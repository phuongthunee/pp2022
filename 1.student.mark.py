print ("STUDENT MARK MANAGEMENT")
print ("")

# Input number of students in a class
def numOfStudents ():
    return int(input("How many students are there in this class?: "))
#-----------------------------------------
# Input student information: id, name, DoB
print ("STUDENT INFORMATION")
def getStudentInfor ():
    Student_ID = input ("ID: ")
    Student_Name = input ("Name: ")
    Student_DoB = input ("DoB (mm/dd/yyyy): ")
    return Student_ID, Student_Name, Student_DoB

inforS = numOfStudents ()
listOfStudents = []
for i in range (inforS):
    Student_ID, Student_Name, Student_DoB = getStudentInfor ()
    print ("")
    inforS = {"Student_ID: ": Student_ID, 
              "Student_Name: ": Student_Name, 
              "Student_DoB: ": Student_DoB,
              "Student_Mark: ": {}}
    listOfStudents.append (inforS)
print ("No.\t ID\t Name\t DoB\t ")
for i in range (0, len(listOfStudents), 1):
    s = listOfStudents[i]
    print ((i+1), "\t", s["Student_ID: "], "\t", s["Student_Name: "], "\t", s["Student_DoB: "])
# List students                         
#-----------------------------------------

#Input number of courses
def numOfCourses ():
    return int(input ("How many courses are there in this class?: "))
#-----------------------------------------
# Input course information: id, name
print ("")
print ("COURSE INFORMATION")
def getCourseInfor ():
    Course_ID = input ("ID: ")
    Course_Name = input ("Name: ")
    return Course_ID, Course_Name

inforC = numOfCourses ()
listOfCourses = []
for i in range (inforC):
    Course_ID, Course_Name = getCourseInfor () 
    print ("") 
    inforC = {"Course_ID: ": Course_ID,
              "Course_Name: ": Course_Name}
    listOfCourses.append (inforC)
print ("No.\t ID\t Name\t ")
for i in range (0, len(listOfCourses), 1):
    s = listOfCourses[i]
    print ((i+1), "\t", s["Course_ID: "], "\t", s["Course_Name: "])
#List courses
#-----------------------------------------

# Select a course, input marks for student in this course
print ("")
print ("SELECT A COURSE, INPUT MARKS FOR STUDENTS IN THIS COURSE")

def selectCourse (listOfCourses):
    listOfCourses = [listOfCourses]
    Course = input ("Select a Course (ID): ")
    return Course

def StudentMark(Course, listOfStudents):
    print (f"Course {Course} - input mark for student: ")
    for inforS in range(0, len(listOfStudents), 1):
        Mark = float(input (f"Student {listOfStudents[inforS] ['Student_ID: ']}: "))
        listOfStudents[inforS]["Student_Mark: "][Course] = Mark  
        
Course = selectCourse(listOfCourses)
StudentMark(Course, listOfStudents)

#-----------------------------------------
# Show student marks for a given course
def showMark(Course, listOfStudents):
    print (f"All marks for the Course {Course}: ")
    for inforS in range(0, len(listOfStudents), 1): 
        print (f"{listOfStudents[inforS]['Student_ID: ']: <20} {listOfStudents[inforS]['Student_Mark: '][Course]}")

Course = selectCourse(listOfCourses)
showMark (Course, listOfStudents)

print ("Done!") 


