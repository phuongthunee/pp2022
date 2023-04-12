import math

class Student: 
    def __init__(self, Student_ID, Student_Name, Student_DoB, Student_Mark):
        self.ID = Student_ID
        self.Name = Student_Name 
        self.DoB = Student_DoB
        self.Mark = Student_Mark
        self.GPA = []
        
    def getStudentInfor(self):
        return self.ID, self.Name, self.DoB
    
    def get_GPA(self):
        return self.GPA
    def set_GPA(self, Student_GPA):
        self.GPA = Student_GPA 
        
class Course:
    def __init__(self, Course_ID, Course_Name, Course_Credits):
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
    Student_Mark = {}
    print ("")
    listOfStudents.append (Student(Student_ID, Student_Name, Student_DoB, Student_Mark))
print ("No.\t ID\t Name\t DoB\t ")
for i in range (0, len(listOfStudents), 1):
    s = listOfStudents[i]
    print ((i+1), "\t", s.ID, "\t", s.Name, "\t", s.DoB)
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
    listOfCourses.append (Course(Course_ID, Course_Name, Course_Credits))
print ("No.\t ID\t Name\t Credit(s)\t")
for i in range (0, len(listOfCourses), 1):
    s = listOfCourses[i]
    print ((i+1), "\t", s.ID, "\t", s.Name, "\t", s.Credit)
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


