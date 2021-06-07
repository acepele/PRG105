age = int(input("How old are you currently?"))
retire_age = int(input("At what age do you want to retire?"))
yearly_income = float(input("What is your yearly income?"))
savings_percentage = float(input("What percent of your income do you save?"))
total_savings = float(input("How much money do you currently have in your savings?"))
retirement_age = 65
print("This projection assumes a 3% raise each year and a 6% yearly return on investment")
print("YEAR      INCOME       SAVINGS CONTRIBUTIONS           TOTAL SAVINGS")
for year in range(1, 16):
    print(format(year))
years_until_retirement = retirement_age - age
while years_until_retirement > 0:
    years_until_retirement -= 1
    income = yearly_income * 1.03
    contribution = income * savings_percentage
    total_savings = total_savings * 1.06
    total_savings += contribution
