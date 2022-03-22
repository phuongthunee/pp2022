class Student: 
    def __init__(self, ID, Name, DoB):
        self.ID = ID
        self.Name = Name
        self.DoB = DoB
        
    def getStudentInfor(self):
        return self.ID, self.Name, self.DoB
        
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
              "Student_DoB: ": Student_DoB}
    listOfStudents.append (inforS)
print ("No.\t ID\t Name\t DoB\t ")
for i in range (0, len(listOfStudents), 1):
    s = listOfStudents[i]
    print ((i+1), "\t", s["Student_ID: "], "\t", s["Student_Name: "], "\t", s["Student_DoB: "])
# List students
#----------------------------------------

class Course:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
        
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
    inforC = {"ID": Course_ID,
              "Name": Course_Name}
    listOfCourses.append (inforC)
print ("No.\t ID\t Name\t ")
for i in range (0, len(listOfCourses), 1):
    s = listOfCourses[i]
    print ((i+1), "\t", s["ID"], "\t", s["Name"])
#List courses
#-----------------------------------------
        
class Mark:
    def __init__ (self, Mark):
        self.Mark = Mark