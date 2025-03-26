# List are the same way as the Javascript array
# Let's make a sandwich
sandwich = ['bread' , 'nuggets' , 'ketchup' , 10]
print('Original -->' , sandwich)
sandwich.pop()
print('One pop up -->', sandwich)
# Let's make a bigger sandwich
sandwich.append('salad')
print("""
Here is All Ingredients of sandwich""")
# let's get the bread first
print("1- {}".format(sandwich[0]))
print("2- {}".format(sandwich[1]))
print("3- {}".format(sandwich[2]))
print("4- {}".format(sandwich[3]))

sandwich[2] = 'Tomato'
print("Update Sandwich")
print("3- {}".format(sandwich[2]))
# Make it split also define the index
# sandwich[0:4] = 'bread'
# print(sandwich)
# print(sandwich[1:4])

# Here for empty the list
# sandwich.remove('salad')
# print(sandwich)
# Clear the list
# sandwich.clear()
# print(sandwich)

# del sandwich[2]
# print(sandwich)


runner_bot = [50,40,30,20,10]
runner_bot.sort()
print("""Sorted Runner Bot Values 
___\\_0___0.//____
First  Step  -> {runner_bots[0]}
Second Step  -> {runner_bots[1]}
Third  Step  -> {runner_bots[2]}
Fourth Step  -> {runner_bots[3]}
 """.format(runner_bots=runner_bot))
index = 0
for key in runner_bot:
    print(f"""{index + 1} Step  -> {key}""")
    index = index + 1
# It's depend on the length of the runner bot
for i in range(len(runner_bot)):
    print(i)

# Join the list
latitude = [34.0 , 23.3 , 45.0]
longitude = [23.1 , 67.34 , 34.23]
location = latitude + longitude
print('Join the longitude or latitude --> ' , location)

# Extend the list
first_names = ['fatima' , 'zainab' , 'noor']
last_name = ['arshad' , 'fatima' , 'fatima']
first_names.extend(last_name)
print('Extend the list --> ' , first_names)