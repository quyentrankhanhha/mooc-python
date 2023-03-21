# Write your solution here
list = []
times = 0
while True:
    word = input("Word:")
    if word in list:
        times += 1
        break
    list.append(word)
print(f"You typed in {len(list)+1-times} different words")


