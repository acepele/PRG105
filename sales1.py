sale_1 = float(input("What were the total sales for Sunday:"))
sale_2 = float(input("What were the total sales for Monday:"))
sale_3 = float(input("What were the total sales for Tuesday:"))
sale_4 = float(input("What were the total sales for Wednesday:"))
sale_5 = float(input("What were the total sales for Thursday:"))
sale_6 = float(input("What were the total sales for Friday:"))
sale_7 = float(input("What were the total sales for Saturday:"))

total_sales_for_the_week = sale_1 + sale_2 + sale_3 + sale_4 + sale_5 + sale_6 + sale_7
average_sales_per_day = total_sales_for_the_week / 7

print("The total amount of sales for the week was: $" + format(total_sales_for_the_week,",.2f"))
print("The average amount of sales per day was: $" + format(average_sales_per_day,",.2f"))
