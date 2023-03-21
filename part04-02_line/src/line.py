# Write your solution here
def line (time, string):
    string = string[:1]
    if (string == ""):
        print("*"*time)
    print(time * string)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(3, "")