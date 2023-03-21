# Write your solution here
ind = int(input("How many items:"))
x = 1
list = []
while x <= ind:
    item = int(input(f"Item {x}:"))
    list.append(item)
    x += 1
print(list)