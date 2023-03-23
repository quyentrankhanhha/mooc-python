# Write your solution here
def create_tuple(x: int, y: int, z: int):
    numbers = [x,y,z]
    numbers.sort()
    return (numbers[0], numbers[len(numbers)-1], sum(numbers))

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))