print ("STUDENT MARK MANAGEMENT")
print ("")
#-----------------------------------------
def numOfStudents ():
    return int(input("How many students are there in this class?: "))

#-----------------------------------------
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
              "Student_DoB: ": Student_DoB}
    listOfStudents.append (inforS)
print ("No.\t ID\t Name\t DoB\t ")
for i in range (0, len(listOfStudents), 1):
    s = listOfStudents[i]
    print ((i+1), "\t", s["Student_ID: "], "\t", s["Student_Name: "], "\t", s["Student_DoB: "])
#-----------------------------------------
def numOfCourses ():
    return int(input ("How many courses are there in this class?: "))

#-----------------------------------------
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
    inforC = {"ID": Course_ID,
              "Name": Course_Name}
    listOfCourses.append (inforC)
print ("No.\t ID\t Name\t ")
for i in range (0, len(listOfCourses), 1):
    s = listOfCourses[i]
    print ((i+1), "\t", s["ID"], "\t", s["Name"])
    
#-----------------------------------------
#-----------------------------------------
def numOfMarks ():
    return int(input ("How many marks do you want to input?: "))

#-----------------------------------------
print ("")
print ("SELECT A COURSE, INPUT MARKS FOR STUDENTS IN THIS COURSE")

def getMarkInfor ():
    Course_ID = input ("Course ID: ")
    Student_ID = input ("Student ID: ")
    Mark = input ("Mark: ")
    return Course_ID, Student_ID, Mark
inforM = numOfMarks ()
marks = []
for i in range (inforM):
    Course_ID, Student_ID, Mark = getMarkInfor ()
    print ("") 
    inforM = {"Course ID": Course_ID,
              "Student ID": Student_ID,
              "Mark": Mark}
    marks.append (inforM)
print ("No.\t ID\t Name\t ")
for i in range (0, len(marks), 1):
    s = marks [i]
    print ((i+1), "\t", s["Course ID"], "\t", s["Student ID"], "\t", s["Mark"])