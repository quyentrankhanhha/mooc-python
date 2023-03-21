# Write your solution here
list = []
a = 1
print("The list is now", list)
while True:
    answer = input("a(d)d, (r)emove or e(x)it:")
    if answer == 'd':
        list.append(a)
        print("The list is now", list)
        a +=1
    elif answer == 'r':
        list.pop(len(list)-1)
        print("The list is now", list)
        a -= 1
    elif answer == 'x':
        print('Bye!')
        break
