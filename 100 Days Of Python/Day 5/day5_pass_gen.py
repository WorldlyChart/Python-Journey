import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*']

des_letters = int(input("How many letters would you like in your password?\n"))
des_symbols = int(input("How many symbols?\n"))
des_numbers = int(input("How many numbers?\n"))

random_letters = random.choices(letters, k = des_letters)
random_symbols = random.choices(symbols, k = des_symbols)
random_numbers = random.choices(numbers, k = des_numbers)
random_pass = random_letters + random_numbers + random_symbols
random.shuffle(random_pass)
final_pass = ''.join(random_pass)

print("here is your new password!\n")
print(final_pass)