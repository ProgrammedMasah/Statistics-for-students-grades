#function to read file
def ReadStudents(Path):
    Fr = open(Path,"r")
    Line = Fr.readlines()
    Students = {}
    for Student in range(2, len(Line)):
        LineSplit = Line[Student].split(",")              
        Students[int(LineSplit[0])] = [str(LineSplit[1]), float(LineSplit[2]),float(LineSplit[3])]
    Fr.close()
    return Students
#function to calculate the Score
def Score(Exam, Practical):
    return Exam*0.7 + Practical*0.3
#fanction to return the result
def isSuccess(Exam, Practical, Score):
    if ((Exam >= 40) and (Practical >= 40) and (Score(Exam, Practical) >= 60)): return True
    else: return False
#function to pass students marks to the function:Score & isSuccess, and store the results in the dictionary
def FinalResults(Students):
    StudentsScore = list(map(lambda x : Score(x[1][1], x[1][2]) , Students.items()))
    StudentsSuccess = list(map(lambda x : isSuccess(x[1][1], x[1][2],Score) , Students.items()))
    StudentsList = list(Students.values())
    IdsStudents = list(Students.keys())
    for i in range(0, len(Students)):
        StudentsList[i].insert(3, StudentsScore[i])
        StudentsList[i].insert(4, StudentsSuccess[i])
        Students[IdsStudents[i]] = StudentsList[i]
    return Students
#function to return dictionary for successful students
def Success(Students):
    StudentsSuccess = dict(filter(lambda x: x[1][4],Students.items()))
    return StudentsSuccess
#function to return dictionary for Failed But Pass Practical Students
def FailedButPassPractical(Students):
    StudentsFailedButPassPractical = dict(filter(lambda x: x[1][4] == False 
                                                 and x[1][2] >= 40 , Students.items()))
    return StudentsFailedButPassPractical
#function to calculate average students scoure
def ScoreMean(Students):
    StudentsList = list(Students.values())
    Sum = 0
    for Student in range(0, len(Students)):
        Sum += StudentsList[Student][3]
    StudentsScoreMean = Sum / len(StudentsList)
    return StudentsScoreMean
#function to print the dictionary
def Display(Students):
    StudentsList = list(Students.values())
    IdsStudents = list(Students.keys())
    print("%1s %15s %10s %15s %10s %10s"%("ID", "Name", "Exam", "Practical" , "Score", "Success"))
    print("_" * 70)
    for Student in range(0, len(Students)):
        Success = "Success" if (StudentsList[Student][4] == True) else "Fail"
        print("%5s %15s %8s %12s %12.2f %10s"%(IdsStudents[Student], StudentsList[Student][0],
                                              StudentsList[Student][1], StudentsList[Student][2],
                                              StudentsList[Student][3],Success))
Dictionary = ReadStudents("students.txt")
print("________________________ Table Of All Students________________________ \n")
NewDictionary = FinalResults(Dictionary)
Display(NewDictionary)
print("\n \n_____________________Table Of Successful Students_____________________ \n")
Result = Success(NewDictionary)
Display(Result)
print ("\n \n_____________Table Of Failed But Pass Practical Students_____________ \n")
Result =  FailedButPassPractical(NewDictionary)
Display(Result)
print("\n \nThe Averege Students Score = %5.2f"%(ScoreMean(NewDictionary)))