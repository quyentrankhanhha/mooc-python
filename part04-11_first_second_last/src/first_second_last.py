# Write your solution here
def first_word(a):
    ind = a.find(" ")
    return a[:ind]
def second_word(b):
    ind = b.find(" ")
    b = b[ind +1:]
    ind = b.find(" ")
    if ind != -1:
        return b[:ind]
    else:
        return b
def last_word(c):
    ind = c.rfind(" ")
    return c[ind+1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "it was"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))