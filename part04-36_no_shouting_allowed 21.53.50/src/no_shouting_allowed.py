# Write your solution here
def no_shouting(list: list):
    newlist = []
    for x in list:
        if not x.isupper():
            newlist.append(x)

    return newlist

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)

    a = ['aaaa', 'Bbbb', 'CCCc', 'ddDd', 'Eeee', 'ffff', 'GggG', 'hhhh']
    test= no_shouting(a)
    print(test)