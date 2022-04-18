class Student: 
    def __init__(self, Student_ID, Student_Name, Student_DoB):
        self.ID = Student_ID
        self.Name = Student_Name 
        self.DoB = Student_DoB
        
    def getStudentInfor(self):
        return self.ID, self.Name, self.DoB
      
class Course:
    def __init__(self, Course_ID, Course_Name):
        self.ID = Course_ID
        self.Name = Course_Name
        
    def getCourseInfor (self):
        return self.ID, self.Name
    
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
    listOfStudents.append (Student(Student_ID, Student_Name, Student_DoB))
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
    print ("") 
    listOfCourses.append (Course(Course_ID, Course_Name))
print ("No.\t ID\t Name\t ")
for i in range (0, len(listOfCourses), 1):
    s = listOfCourses[i]
    print ((i+1), "\t", s.ID, "\t", s.Name)
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


