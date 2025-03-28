import random

# Dictionary
# Real chatting

# user_name = input("Enter You Name:")
# responses = [
#     "How can I assist you today?",
#     "What would you like help with?",
#     "Is there anything specific you need?",
#     "Tell me how I can help you.",
#     "I'm here to assist, just ask!"
# ]
# bot = {
#     "message":"""Hey {name} : {response} """.format(name = user_name , response = random.choice(responses))
# }
# while True:
#     user_response = input(bot["message"] + " ")
#     if user_response.lower() in ['exist' , "quite" , 'bye']:
#          print("GoodBye!!")
#          break


comment = {
    "id":1,
    "message" :"Hello!!",
    "email" :"fatima@gmail.com"
}
print(comment["message"])
for_value = comment.values()
print('It display in the list-->' ,for_value)
# convert to the list
change = list(for_value)
print(change[1])
for_keys = comment.keys()
print('It display in the list-->' ,for_keys)
for_items = comment.items()
print('Items are in the list / the property or the value added in th tuple-->',for_items)

# Sets are unordered , no duplicate , unchangeable
new_user = {"fatima" , "fatima@gmail.com" , 21}
for data in new_user:
    print(data)
new_user.add('computer science')
user_1 = {"noor"}
# new_user.update(user_1)
# new_user.remove('fatima')
# new_user.pop()

store = new_user.union(user_1)
new_data = new_user | user_1
print(new_data)
