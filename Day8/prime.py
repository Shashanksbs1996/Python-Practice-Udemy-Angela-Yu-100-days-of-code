#Write your code below this line 👇
from tkinter.tix import Tree


def prime_checker(number):
    flag = True
    for i in range(2,number):
        if number%i==0:
            flag= False
            
        
    if flag==True:
      print("It's a prime number.")
    else:
      print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
