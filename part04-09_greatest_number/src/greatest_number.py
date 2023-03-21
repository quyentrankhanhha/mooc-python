# Write your solution here
def greatest_number(a,b,c):
    flag = a
    if flag < b:
        flag = b
    if flag < c:
        flag = c
    return flag

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(3, 5, 7)
    print(greatest)