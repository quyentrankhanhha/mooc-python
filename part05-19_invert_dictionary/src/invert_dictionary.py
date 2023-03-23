# Write your solution here
def invert(dictionary: dict):
    new_dic = {}
    for key,value in dictionary.items():
        new_dic[value] = key
    dictionary.clear()
    for key,value in new_dic.items():
        dictionary[key] = value

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)