# Write your solution here
def spruce(num):
    print("a spruce!")
    quantity = 1
    i = num -1
    while num > 0:
        print(" " * (num-1) + '*'*quantity )
        num -=1
        quantity +=2
    print(" " * i + '*' )

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)