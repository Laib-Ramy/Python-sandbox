import re

def check_address():
    # Get the first email input
    email = input("Enter email: ")
    pattern='^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
    # Loop to check the email input until the user quits or provides a valid email
    while email:
        if email.lower() in ["quit", "exit", "basta"]:
            print("Bye!")
            break
        elif re.fullmatch(pattern, email, re.IGNORECASE):
            print("OK")
            return email
        else:
            print("Try again")
            email=input()
        

if __name__=='__main__':
    check_address()