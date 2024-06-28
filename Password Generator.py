import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters = int(input("How many Letters You want? "))
n_numbers = int(input("How many Numbers You want? "))
n_symbols = int(input("How many Symbols You want? "))

password_list = []
for letter in range(1, n_letters+1):
    password_list.append(random.choice(letters))
for number in range(1,n_numbers+1):
    password_list.append(random.choice(numbers))
for symbol in range(1,n_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = " "
for ch in password_list:
    password += ch

print(f"Your Generated password is: {password}")





