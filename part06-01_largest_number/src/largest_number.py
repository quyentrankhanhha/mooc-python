# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        
        for number in new_file:
            if int(number) > int(largest):
                largest = number
    return int(largest)

if __name__ == "__main__":
    largest()
    