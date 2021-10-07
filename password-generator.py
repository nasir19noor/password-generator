import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '<', '>', '?' ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Password Generator\n")
number_letters = int(input("How many letters would you like in your password? "))
number_symbols = int(input("How many symbols would you like in your password? "))
number_numbers = int(input("How many number would you like in your password? "))

password_letters = ""
password_symbols = ""
password_numbers = ""
password_total_1 = ""
total_numbers = 0

for i in range(0, number_letters):
  random_number = random.randint(0, 11)
  password_letters += letters[random_number]
  print(letters[random_number])
total_numbers += number_letters
print(password_letters)
print(total_numbers)

for i in range(0, number_symbols):
  random_number = random.randint(0, 11)
  password_symbols += symbols[random_number]
  print(symbols[random_number])
total_numbers += number_symbols
print(password_symbols)
print(total_numbers)

for i in range(0, number_numbers):
  random_number = random.randint(0, 9)
  password_numbers += numbers[random_number]
  print(numbers[random_number])
total_numbers += number_numbers
print(password_numbers)
print(total_numbers)

password_total_1 = password_letters + password_symbols + password_numbers
print(password_total_1)

password_total_2 = list(password_total_1)
print(password_total_2)
random.shuffle(password_total_2)

password_total_3 = ''.join(password_total_2)
print(password_total_3)
