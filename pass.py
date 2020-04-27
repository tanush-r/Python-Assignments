from random import *
import string

def random_list(l,n):
    
    return_list = []
    
    for i in range(n):
        
        element = choice(l)
        return_list.append(element)
        
    return return_list


letters = string.ascii_letters
numbers = ''.join(map(str, range(0, 10)))
special_characters = '.,/?!@£$%^&*()\\;:{}[]-_=+~`#'

print("Welcome to password generator!\n\n")
print("Enter how many letters, numbers and special characters you want and a random password will be generated for you")

letter_num = number_num = special_num = 0

while True:
    
    letter_num = int(input("How many letters?"))
    number_num = int(input("How many numbers?"))
    special_num = int(input("How many special characters?"))
    if letter_num + number_num + special_num < 8:
        print("Password count should be greater than 8")
    else:
        break
    
let = random_list(letters,letter_num)
num = random_list(numbers,number_num)
spe = random_list(special_characters,special_num)
pas = let + num + spe
shuffle(pas)
pass_final = "".join(pas)
print("Generated password :",pass_final)

