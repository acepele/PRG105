student = input("Are you a new or returning student? Please enter n or r:")
GPA_calculation = float(input("What is your current GPA?"))
credit_hour_classes = int(input("How many credit hours are you enrolled for next semester?"))
gross_yearly_income = int(input("What is your gross yearly income,rounded to the nearest dollar?Don't use commas: "))
history = input("Have you ever been convicted of a drug felony? Please enter y or n: ")
if GPA_calculation >= 6 and gross_yearly_income < 50000 and credit_hour_classes >= 6:
    print("you are eligible for financial aid")
else:
    print("you are not eligible for financial aid")
