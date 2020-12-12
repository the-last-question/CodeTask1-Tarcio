def __isPalindrome(string):
    return string == string[::-1]

def __main__():
    word = input("Enter the word you want to check: ")
    if(__isPalindrome(word)):
        print(word + " is a palindrome!")
    else:
        print(word + " isnt palindrome!")
        
__main__()