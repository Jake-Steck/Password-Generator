import random
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
password = ""
rang = int(input("How many character would you like your password to be? "))
for i in range(rang):
  password += random.choice(char)
print(password)
