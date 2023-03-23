# Write your solution here
phonebook = {}

while True:
    cmd = int(input("command (1 search, 2 add, 3 quit):"))

    if cmd == 3:
        print("quitting...")
        break

    elif cmd == 1:
        name = str(input("name: "))
        if name not in phonebook:
            print("no number")
        else:
            for key, value in phonebook.items():
                if key == name:
                    for i in value:
                        print(i)
             
    elif cmd == 2:
        name = str(input("name: "))
        phone = str(input("number: ")) 
        if name not in phonebook:
            phonebook[name] = [] 
        phonebook[name].append(phone)
        print("ok!")
        
