# Write your solution here
def list_sum(a,b : list):
    c = []
    indexa = 0
    indexb = 0

    while indexa < len(a):
        while indexb < len(b):
            if (indexa == indexb):
                print(a[indexa])
                print(b[indexb])
                c.append(a[indexa] + b[indexb])
            indexa += 1
            indexb += 1

    return c

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))