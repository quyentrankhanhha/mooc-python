# wite your solution here

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

names = {}
with open(f"{student_info}") as student_file:
    for line in student_file:
        line = line.replace("\n", "" )
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        names[parts[0]] = parts[1] + " " +  parts[2]

exercises = {}
with open(f"{exercise_data}") as exercise_file:
    for line in exercise_file:
        line = line.replace("\n", "" )
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        exercises[parts[0]]= []

        for part in range(1,8):
            exercises[parts[0]].append(int(parts[part]))

exams = {}
with open(f"{exam_data}") as exam_file:
    for line in exam_file:
        line = line.replace("\n", "" )
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        exams[parts[0]] =[]

        for part in range(1,4):
            exams[parts[0]].append(int(parts[part]))

totalInfo = {}
for nameId, fullName in names.items():
    for examId, totalExam in exams.items():
        if nameId == examId:
            totalInfo[nameId] = [fullName, sum(totalExam)]
    for exerciseId, totalExer in exercises.items():
        if nameId == exerciseId:
            sumExer = float(sum(totalExer)/40 * 100)
            gradeExer = 0
            if sumExer < 10:
                gradeExer = 0
            elif sumExer < 20:
                gradeExer = 1
            elif sumExer < 30:
                gradeExer = 2
            elif sumExer < 40:
                gradeExer = 3
            elif sumExer < 50:
                gradeExer = 4
            elif sumExer < 60:
                gradeExer = 5
            elif sumExer < 70:
                gradeExer = 6
            elif sumExer < 80:
                gradeExer = 7
            elif sumExer < 90:
                gradeExer = 8
            elif sumExer < 100:
                gradeExer = 9
            else:
                gradeExer = 10
            total = totalInfo[nameId][1] + gradeExer
            if total <= 14: 
                print(totalInfo[nameId][0] + " 0")
            elif total <= 17:
                print(totalInfo[nameId][0] + " 1")
            elif total <= 20:
                print(totalInfo[nameId][0] + " 2")
            elif total <= 23:
                print(totalInfo[nameId][0] + " 3")
            elif total <= 27:
                print(totalInfo[nameId][0] + " 4")
            else:
                print(totalInfo[nameId][0] + " 5")

