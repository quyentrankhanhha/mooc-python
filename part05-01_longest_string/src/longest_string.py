# Write your solution here
def longest(strings: list):
    num = 0
    string = ""
    for i in strings:
        if len(i) > num:
            num = len(i)
            string = i
    return string
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))