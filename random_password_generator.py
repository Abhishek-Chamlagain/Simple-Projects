import random
import string

allchar=string.ascii_letters + string.digits + string.punctuation

while True:
    try:
          user_input=int(input("Enter length for password: "))
    except ValueError:
            print("Please enter a valid number")
            continue
    
    if user_input <= 0:
        print("Password length must be greater than 0")
        continue

    random_password = ""
    for i in range(user_input):
         random_password += random.choice(allchar)
          
    print("Random password is: ",random_password)
    break

