# Write your solution here
def everything_reversed(mylist: list):
    result = []
    i = len(mylist) - 1
    while i>=0:
        result.append(mylist[i][::-1])
        i -= 1

    return result

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)