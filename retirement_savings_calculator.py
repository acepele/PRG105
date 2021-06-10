age = int(input("How old are you currently?"))
retire_age = int(input("At what age do you want to retire?"))
income = float(input("What is your yearly income?"))
percentage = float(input("What percent of your income do you save?"))
savings = float(input("How much money do you currently have in your savings?"))

pay_raise = .03
investment = .06
years_until_retirement = retire_age - age
print("You have " + str(years_until_retirement) + " years left until you retires")
year = 0

print("This projection assumes a 3% raise each year and a 6% yearly return on investment")
print("    YEAR        INCOME          SAVINGS CONTRIBUTIONS           TOTAL SAVINGS")
while year < years_until_retirement:
    year += 1
    income += pay_raise * income
    total_savings = savings * investment
    contribution = income * percentage
    years_until_retirement -= 1
    total_savings += contribution
    print(format(year, "8,.0f") + format(income, "14,.0f") + format(contribution, "25,.0f")
          + format(total_savings, "30,.0f"))
