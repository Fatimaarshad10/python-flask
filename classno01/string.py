# String 
# Single line
job_title = "Software Engineer"
job_description = "Must have a 2 year experience"
print(job_title)
print(job_description)

# Multiple line 
user_name = "fatima"
user_detail = """Hey I'm Fatima Arshad. 
I'm a Web and mobile development
 instructor!!"""
print(user_detail)

# Variable or the string
user_age = 21
print(f"{user_name} age is {user_age} :)")
upper_word = user_name.upper()
print('Name is in the UpperCase --->' , upper_word)

# concat the string
print('Fatima' + 'Arshad')
print('Noor' + " " + '- ul' + " " + "- fatima")

# Get the string character 
print(user_detail[0])
print(user_detail[9])

# Check the length of the string 
check_length = len(user_detail)
print("User detail length" , check_length)

# In the description only the 30 character should be write 
# For that make the condition on that 
if(check_length <= 30):
    print("You can write more character")
else:
    print("Length Exceeded!")

skill_name = "html,css,js,python,reactjs,nextjs"
token = " token is expired         "

# slice
print(skill_name[0:5])
print(skill_name[7:10])

# split
print(token.split())
print(skill_name.split(','))

# remove the whitespace
print(token)
print(token.strip())

# Make the lowercase 
print(upper_word.lower())


# format()
# Html basic structure 
paragraph_size = 30
paragraph_color = 'red'
print('Html First paragraph size is {} and the color is {} '.format(paragraph_size , paragraph_color))

# unintentionally if I call the first one at the second place then it is not helpful
# It's wrong 
print("paragraph color is {} and the size is {}".format(paragraph_size , paragraph_color))

print("""
Image tag have the width and the height attribute
let's initialize in html tag 
<img src={source} alt={alternate_name} width={width} height={height} />
""".format(source='./fatima.jpg' , alternate_name='fatima_img' , width='50px' , height='50px'))

# Index base access the variables
print("""let's make the calculator:
function add({0},{1})
return {2}""".format(10,20 , 10+20))

# float value in format
money_in_dollar = 40.6500
print("Dollar rate is {:.2f}".format(money_in_dollar))

# Boolean
store_boolean = bool('fatima')
print(store_boolean)
print(bool())

# Check the authentication role
# role = 'user admin'
# new_array = role.split()
# print('You have two role you can select one of them' , new_array)
# user_role = input("Role_______:")
# if(user_role == 'admin'):
#     print("Navigate to the dashboard page")
# else:
#     print("Navigate to the Home page")













