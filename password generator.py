import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)
char=[]


#Main program starts here
n=input("how many characters do you want?")
n=int(n)
password=""


for i in range(n):#Generate a random char
    char.append(chr(random.randint(33,191))) 
    password = password+char[i]
password = shuffle(password)

#Ouput
print(password)
