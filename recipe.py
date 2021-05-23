# Cookies recipe
print("Easy Sugar Cookies ")
print("Ingredients used for this recipe")
print("Flour")
print("Baking soda")
print("Baking powder")
print("Butter")
print("Sugar")
print("Egg")
print("Vanilla extract")
# Data
COOKIES = 48
FLOUR = 1.5
BAKING_SODA = 5.69
BAKING_POWDER = 2.84
BUTTER = 128
SUGAR = 192
EGGS = 1
VANILLA_EXTRACT = 5.69
# Processing
number_of_cookies = int(input('How many cookies would you like to make: '))
total_flour = (FLOUR * number_of_cookies) / COOKIES
total_baking_soda = (BAKING_SODA * number_of_cookies) / COOKIES
total_baking_powder = (BAKING_POWDER * number_of_cookies) / COOKIES
total_butter = (BUTTER * number_of_cookies) / COOKIES
total_sugar = (SUGAR * number_of_cookies) / COOKIES
total_eggs = (EGGS * number_of_cookies) / COOKIES
total_vanilla_extract = (VANILLA_EXTRACT * number_of_cookies) / COOKIES
# Output
print('\nNumber of cookies =', number_of_cookies, end='\n\n')
print('Total flour =', format(total_flour, ',.1f'))
print('Total baking powder =', format(total_baking_powder, ',.1f'))
print('Total baking soda =', format(total_baking_soda, ',.1f'))
print('Total butter =', format(total_butter, ',.1f'))
print('Total sugar =', format(total_sugar, ',.1f'))
print('Total eggs =', format(total_eggs, ',.1f'))
print('Total vanilla extract =', format(total_vanilla_extract, ',.1f'), end='\n\n')
