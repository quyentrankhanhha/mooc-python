# Write your solution here
def histogram(words: str):
    result = {}
    for word in words:
        if word not in result:
            result[word] = ""
        result[word] += "*"
    for key, value in result.items():
        print(key, value)
    return 

if __name__ == "__main__":
    histogram("abba")    
