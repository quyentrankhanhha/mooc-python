# write your solution here
text = input("Write text: ")
parts = text.split(" ")

words = []
with open("wordlist.txt") as word_file:
    for line in word_file:
        line = line.replace("\n", "" )
        words.append(line)

for part in parts:
    if part.lower() not in words:
        index = parts.index(part)
        parts[index] = "*" + part + "*"

result = ' '.join(parts)
print(result)