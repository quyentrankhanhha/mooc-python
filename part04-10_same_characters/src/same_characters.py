# Write your solution here
def same_chars(text, a,b):
    if  len(text)> a and len(text)>b and text[a] == text[b] :
        return True
    else:
        return False
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))