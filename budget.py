total_net_monthly_income = float(input("What is your total net monthly income?"))
housing = float(input("How much do you spend on housing each month?"))
food = float(input("How much do you spend on food each month?"))
transportation = float(input("How much do you spend on transportation each month?"))
phone = float(input("How much do you spend on your phone bill each month?"))
utilities = float(input("How much do you spend on your utilities each month?"))
clothing = float(input("How much do you spend on clothing each month?"))

total_expenses = housing + transportation + phone + utilities + clothing

housing_expenses = ((housing / total_net_monthly_income) * 100.0)
print("Housing takes up", format(housing_expenses, ',.2f') + "%"    " of your monthly budget")

food_expenses = ((food / total_net_monthly_income) * 100.0)
print("Food takes up", format(food_expenses, ',.2f') + "%"      " of your monthly budget")

transportation_expenses = ((transportation / total_net_monthly_income) * 100.0)
print("Transportation takes up", format(transportation_expenses, ',.2f') + "%"    " of your monthly budget")

phone_expenses = ((phone / total_net_monthly_income) * 100.0)
print("Phone bill takes up", format(phone_expenses, ',.2f') + "%"    " of your monthly budget")

utilities_expenses = ((utilities / total_net_monthly_income) * 100.0)
print("Utilities take up", format(utilities_expenses, ',.2f') + "%"    " of your monthly budget")

clothing_expenses = ((clothing / total_net_monthly_income) * 100.0)
print("Clothing takes up", format(clothing_expenses, ',.2f') + "%"    " of your monthly budget")

amount_left = (total_net_monthly_income - total_expenses)
print("You have $" + format(amount_left), " left from your income after paying these monthly expenses.")
