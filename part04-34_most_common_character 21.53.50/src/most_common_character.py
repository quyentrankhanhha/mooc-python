# Write your solution here
def most_common_character(mystring: str):
    flag = 0
    character =""
    for i in mystring:
        mystring.count(i)
        if (mystring.count(i) > flag):
            flag = mystring.count(i)
            character = i
    return character


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))