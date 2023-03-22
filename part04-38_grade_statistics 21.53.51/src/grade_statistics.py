# Write your solution here
import math

def input_from_user():
    i = 1
    numbers = []
    while i > 0:
        number = input("Exam points and exercises completed:")
        if (number == ""):
            break
        number = number.split(" ", 1)
        if 0 <= int(number[0]) <= 20 and 0 <= int(number[1]) <= 100:
            numbers.append(int(number[0]))
            numbers.append(int(number[1]))
        else:
            break
    return numbers

def count_grade(exam_point : int, exer_point: int):
    total = exam_point + exer_point
    if exam_point < 10 or total <= 14:
        grade = 0
    elif 15 <= total <= 17:
        grade = 1
    elif 18 <= total <=20:
        grade = 2
    elif 21 <= total <= 23:
        grade = 3
    elif 24 <= total <= 27:
        grade = 4
    else:
        grade = 5
    return grade

def statistics(grades: list, points: list):
    failed_point = grades.count(0)
    print("Statistics:")
    print(f"Points average: {sum(points)/len(points)}")
    print(f"Pass percentage: {round((len(grades)- failed_point)/len(grades)*100, 1)}")
    print("Grade distribution:")
    for i in range(5,-1,-1):
        print(f"{i}: {grades.count(i)* '*'}")

def main():
    numbers = input_from_user()
    points = []
    grades = []
    x = 0
    while x < len(numbers):
        if x == 0 or x % 2 == 0:
            exam_point = numbers[x]
            exer_point = math.floor(numbers[x+1]* 0.1)
            grade = count_grade(exam_point,exer_point) 
            grades.append(grade)
            points.append(exam_point + exer_point) 

        x += 1 
    statistics(grades, points)

main()