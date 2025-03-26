# Tuple is unmutable
import random
shoe = ('black' ,'girlish' , 3500)
print(shoe[1])
# Add values
change_shoe = list(shoe)
change_shoe.append('Rupees')
shoe = tuple(change_shoe)
print(shoe)
(black , *red) = shoe
print(black)
print(red)
# join the Tuple
new_shoes = shoe * 2
print(new_shoes)

# Dictionary
first_name = input("First_name _____ :")
last_name = input("Last_name _____ :")
email = input("email _____ :")
password = input("password _____ :")
user = {
     "first_name" : first_name,
    "last_name" : last_name ,
    "email" : email,
    "password": password,
    "is_verified" : random.choice([True, False])
}

if(user['is_verified'] == True):
    print("User is Registered Status Code is 200", user)
else:
    print("Otp is sent! Check your mail", "Verified this : 1234123")

comments = {
    "id" : 1,
    "message":"Hello"
}

print(type(comments))
