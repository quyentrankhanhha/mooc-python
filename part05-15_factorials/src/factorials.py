# Write your solution here
def factorials(n: int):
    result = 1
    obj = {}
    for i in range(1,n+1):
        result *=i
        obj[i] = result

    return obj

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
