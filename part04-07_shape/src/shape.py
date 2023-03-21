# Copy here code of line function from previous exercise and use it in your solution
def line (time, string):
    if (string == ""):
        string='*'
    print(time * string[0])

def shape(width, characterA, height, characterB):
    x = 1
    while x <= width:
        line(x, characterA)
        x += 1

    y = height
    while y > 0:
        line(width, characterB)
        y -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")