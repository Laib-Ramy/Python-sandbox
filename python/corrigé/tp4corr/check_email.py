import re

def check_address():
    p1=r"^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$"
    p2=r"^(quit|exit|basta)$"
    while True:
        str=input("Enter an e-mail: ")
        if re.match(p2, str):
            print('Bye!')
            return
        if re.match(p1, str):
            print('OK')
            return str
        else:
            print('Try again')

if __name__=='__main__':
    check_address()