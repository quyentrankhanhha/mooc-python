# Write your solution here
def all_the_longest(my_list: list):
    new_list = []
    result = []
    length = 0
    for item in my_list:
        if (len(item) >= length):
            length = len(item)
            new_list.append(item)
    for item in new_list:
        if (len(item) >= length):
            result.append(item)
    return result


if __name__ == "__main__":
    my_list = ["abc", "ab"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']