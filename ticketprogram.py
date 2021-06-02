print("1. Student $5.00")
print("2. Veteran $7.00")
print("3. Show sponsor $2.00")
print("4. Retiree $6.00")
print("5. General public $10\n")
category = int(input("Please enter the number of the category of the purchaser: "))
if category == 1:
    price = 5.00
elif category == 2:
    price = 7.00
elif category == 3:
    price = 2.00
elif category == 4:
    price = 6.00
else:
    price = 10.00
print("The price per ticket is: $", format(price))
number_ticket = int(input("How many ticket would you like to purchase? "))
if number_ticket > 15:
    discount = .2
elif number_ticket > 8:
    discount = .15
elif number_ticket > 4:
    discount = .10
else:
    discount = 0
print("You have a discount of ", format(discount))
total_price = price * number_ticket
discount_amt = total_price * discount
total_after_discount = total_price - discount_amt

print("Total cost before any discount is applied is:$", format(total_price))
print("Total cost after your discount is applied is:$", format(total_after_discount))
