total = 0
for day in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
    sales = float(input("What were the total sales for '+ day +' :"))
    total += sales
print("The total amount of sales for the week was: " + format(total, ",.2f"))
print("The average amount of sales for the day was:" + format(total / 7, ",.2f"))
