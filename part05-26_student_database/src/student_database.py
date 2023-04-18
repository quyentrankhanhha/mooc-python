# Write your solution here
def add_student(students: dict, name:str):
    new_student = []
    students[name]= new_student
    return students

def add_course(students:dict, name: str, course: tuple):
    nameCourse = ''
    gradeCourse = 0

    for item in course:
        if type(item) == str:
            nameCourse = item

        if type(item) == int and item == 0:
            return
        elif type(item) == int and item != 0:
            gradeCourse = item
      
    if len(students[name]) == 0:
        students[name].append(course)  
        return
    else:
        for enrolledCourse in students[name]:
            if nameCourse == enrolledCourse[0] and gradeCourse > enrolledCourse[1]:
                course = [enrolledCourse[0], enrolledCourse[1]]
                courseTuple = tuple(course)
                students[name].remove(courseTuple)

                courseList = list(enrolledCourse)
                courseList[1] = gradeCourse
                enrolledCourse = tuple(courseList)
                students[name].append(enrolledCourse)

                return enrolledCourse
            elif nameCourse == enrolledCourse[0] and gradeCourse < enrolledCourse[1]:
                return
            elif enrolledCourse[0] != nameCourse:
                students[name].append(course) 
                return 

def print_student(students: dict, name: str):
    average = []

    if name in students and students[name] != []: 
        print(name + ":")
        print("",len(students[name]), "completed courses:")
        for course in students[name]:
            for item in course:
                if type(item) == str:
                    print(" ",item, end=" ")
                if type(item) == int:
                    print(item)
                    average.append(item)

        grade = sum(average) / len(average)
        print(" average grade", grade)   

    elif name in students and students[name] == []:
        print(name + ":")
        print(" no completed courses")
    else:
        print(name + ": no such person in the database")

def summary(students: dict):
    print("students", len(students))
    mostCourseName = ''
    mostCourseNumber = 0
    bestGrade = 0
    bestStudent = ''
    for student in students:
        average = []

        if mostCourseNumber < len(students[student]):
            mostCourseNumber = len(students[student])
            mostCourseName = student
        for item in students[student]:
            for detail in item:
                if type(detail) == int:
                    average.append(detail)
        grade = sum(average) / len(average)
        if bestGrade < grade:
            bestGrade = grade
            bestStudent = student
    print("most courses completed", mostCourseNumber, mostCourseName)
    print("best average grade", bestGrade, bestStudent)

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 5))
    print_student(students, "Peter")
