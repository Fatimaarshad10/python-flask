import random

# While Loops
# When we don't know how many times it will run, we use a while loop
year = 2001
while year < 2010:
    year = year + 1
    print(year)
    if year == 2003:
        print("Bad Year Let's look more....")
        continue
    if year == 2005:
        print("Good year :)")
        break
else:
    print("ALl Ended")

# For Loop
main_list = [1,2,3,4,5,6,7,8,9,10]
main_tuple = ("id" , "title", "description" , "created_by" , "updated_by")
main_dic = {"sender":"noor" , "receiver":"fatima"}
main_set = {'first' , 'second', 'third'}
for tupe_data in main_tuple:
    if tupe_data == random.randint(1,10):
        print("Your Lucky no:" ,tupe_data)
        break
    else:
        print("Your Unlucky no" , tupe_data)

number = 10
for i in range (1,100):
    if number > i:
        print('Just Random no --> ' , i)
for key , value in main_dic.items():
    print(key , value)

# functions
def turn_right():
    first_step = 1 + 1
    return first_step
value = turn_right()
print(value)

def jwt_token(value):
    separate_value = value.split(' ')
    new_value = random.choice(separate_value)
    for i in separate_value:
        if i == new_value:
            print("JWT Token random value--->" , i)

jwt_token('Here is the value')


def sum_fun(a ,b):
    return a + b

def calculate(first = 10 ,second = 10):
    print(sum_fun(first,second))

calculate()

def names (*all):
    print(all)
names('fatima' , 'zainab')

# Lambda functions
