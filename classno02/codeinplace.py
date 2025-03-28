
# An earthling's weight on Mars is 37.8% of their weight on earth.
# Write a Python program that prompts the user (an earthling)
# to enter their weight on earth and prints their calculated weight on Mars

# Sample
# Enter a weight on earth: 120
# The equivalent weight on Mars: 45.36

MARS_MULTIPLE = 0.378
earth_weight = input("Enter a weight on earth:")
earth_weight_float = float(earth_weight)
# calculate the mars weight
store_mars_weight = earth_weight_float * MARS_MULTIPLE
print('The equivalent weight on Mars:' , str(store_mars_weight))


# def main():
#     earth_weight_str = input('Enter a weight on earth: ')
#     earth_weight = float(earth_weight_str)
#     mars_weight = earth_weight * MARS_MULTIPLE
#     print('The equivalent weight on Mars: ' + str(mars_weight))
# main()