# Write your solution here
def oldest_person(people: list):
    year = people[1][1]
    for i in people:
        if year > i[1]:
            year = i[1]
    
    return 

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    print(oldest_person(people))