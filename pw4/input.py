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
        