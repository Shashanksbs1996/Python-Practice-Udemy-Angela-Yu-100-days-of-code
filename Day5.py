#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# for i in range(2):
#     rletter=random.choice(letters)
#     rsymbol = random.choice(numbers)
#     rnumber = random.choice(symbols)
# print(f"Your new Password is : {rletter}{rsymbol}{rnumber}")
lst =[]
for i in range(nr_letters):
    rletter=random.choice(letters)
    lst.append(rletter)
print(lst)


for i in range(nr_symbols):
    rsymbol=random.choice(symbols)
    lst.append(rsymbol)
print(lst)


for i in range(nr_numbers):
    rnumbers=random.choice(numbers)
    lst.append(rnumbers)
print(lst)

print("This is a ***Easy password*** ")
print(f"Your new Password is : {lst}")

print("This is a ***Hard password***")
reran = random.shuffle(lst)
print(f"Your New Password is : {lst}")

password = ""
for char in lst:
    password += char

print(f"\n \n \nHere is your final Password: {password}")