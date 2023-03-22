# Write your solution here
def shortest(list: list):
    length = len(list[0])
    word =""
    for item in list:
        if (len(item) <= length):
            length = len(item)
            word = item
    return word

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)