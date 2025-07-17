'''
Use case:
I have a hotel and whoever is login ask the user to provide the inputs and their inputs
such as Name , fav food , fav vacation type and print this welcome note to their customers
'''

'''================================================================='''

name = input("Please provide your name: ")
#print(name)
food = input("what's your favourite food: ")
#print(food)
vacation = input("what's your vacation type: ")
#print(vacation)
hotel_name = "Taj Banjara"

print(f"Hello {name}, Welcome to Hotel {hotel_name}, Enjoy your favourite food  {food},"
      f"When would you like to visit {vacation} for refreshment")