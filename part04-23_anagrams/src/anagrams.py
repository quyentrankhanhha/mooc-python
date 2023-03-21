# Write your solution here
def anagrams(a,b):
    a = sorted(a)
    b = sorted(b)
    if a==b:
        return True
    else:
        return False
if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False