import math

class Student: 
    def __init__(self, Student_ID, Student_Name, Student_DoB, StudentMark):
        self.ID = Student_ID
        self.Name = Student_Name 
        self.DoB = Student_DoB
        self.Mark = StudentMark
        self.GPA = 0
        
    def getStudentInfor(self):
        return self.ID, self.Name, self.DoB
    
    def get_GPA(self):
        return self.GPA
    def set_GPA(self, Student_GPA):
        self.GPA = Student_GPA 
        
class Course:
    def __init__(self, Course_ID, Course_Name, Course_Credits,):
        self.ID = Course_ID
        self.Name = Course_Name
        self.Credit = Course_Credits
        
    def getCourseInfor (self):
        return self.ID, self.Name
    
    def gpa (self):
        return self.Credit + self.Mark
    
class Mark:
    def __init__ (self, Mark):
        self.Mark = Mark
        
#-----------------------------------------   
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
print ("No.\t ID\t Name\t ")
for i in range (0, len(listOfCourses), 1):
    s = listOfCourses[i]
    print ((i+1), "\t", s["ID"], "\t", s["Name"])
#List courses
#-----------------------------------------

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
        
#-----------------------------------------
# Show student marks for a given course
selectCourse = input("Which course do you want to see all student marks?: ")
if selectCourse in StudentMark:
    print (f"Course {selectCourse} mark: ")    
    for i in range (len(numOfStudents)):
        print (f"Student {Student_ID[i]}: {StudentMark[selectCourse][i]}")
else:
    print ("Wrong! Input again...")  
    
StudentMark.sort(key = len)
print (math.floor(StudentMark))    
    
print ("Done!")