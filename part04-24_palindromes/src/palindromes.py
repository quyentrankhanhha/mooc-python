# Write your solution here
def palindromes(text:str):     
    text = text.replace(" ", "").lower()
    return text == text[::-1]
    
def main(text):
    while True:
        text = input("Please type in a palindrome: ")    
        if palindromes(text):
            print(text, "is a palindrome!")
            return
        else:      
            print("that wasn't a palindrome")
        
# Note, that at this time the main program should not be written inside
main(text=None)
