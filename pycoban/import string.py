import string;
ascii = string.ascii_letters
alpha = string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
ALPHA = string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
digit = string.digits
if __name__ == '__main__':
    s = input()
    check = False
    if any(x in ascii for x in s):
        if any(x in digit for x in s):
            print("True")
            check = True
    if check == False : print("False")
    check = False
    if any(x in ascii for x in s):
        print("True")
        check = True
    if check == False: print("False")
    check = False
    if any(x in digit for x in s):
        print("True")
        check = True
    if check == False: print("False")
    check = False
    if any(x in alpha for x in s):
        print("True")
        check = True
    if check == False: print("False")
    check = False
    if any(x in ALPHA for x in s):
        print("True")
        check = True
    if check == False: print("False")
    
        
    
    