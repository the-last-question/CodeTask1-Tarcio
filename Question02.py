import re #regular expression library import

def __checkPassword(password):
    checker = 0
    while True:   
        if (len(password)<8): 
            checker = -1
            break
        elif not re.search("[a-z]", password): 
            checker = -1
            break
        elif not re.search("[A-Z]", password): 
            checker = -1
            break
        elif not re.search("[0-9]", password): 
            checker = -1
            break
        elif re.search("\s", password): 
            checker = -1
            break
        else: 
            checker = 0
            return True
    
        if checker ==-1:
            return False

def __main__():
    password = input("Enter the password: ")
    if(__checkPassword(password)):
        print("this is a valid password")
    else:
        print("this is a invalid password")
        
__main__()