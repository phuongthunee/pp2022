print ("No.\t ID\t Name\t DoB\t ")
for i in range (0, len(listOfStudents), 1):
    s = listOfStudents[i]
    print ((i+1), "\t", s["Student_ID: "], "\t", s["Student_Name: "], "\t", s["Student_DoB: "])

print ("No.\t ID\t Name\t ")
for i in range (0, len(listOfCourses), 1):
    s = listOfCourses[i]
    print ((i+1), "\t", s["ID"], "\t", s["Name"])

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