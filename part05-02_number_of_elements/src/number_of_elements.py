# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    times = 0
    for i in my_matrix:
        times += i.count(element)
    return times
if __name__ == "__main__":

    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))