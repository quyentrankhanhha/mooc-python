# write your solution here

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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

        
for nameId, fullName in names.items():
    for exerciseId, totalExer in exercises.items():
        if nameId == exerciseId:
            print(fullName, sum(totalExer))
