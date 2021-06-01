eligible_for_financial_aid = True
student_status = input("Are you a new or returning student? Please enter n or r: ")
if student_status == "r" or student_status == "n":
    gpa = float(input("What is your current gpa?: "))
    if gpa < 2.0:
        eligible_for_financial_aid = False
criminal_record = input("Have you ever been convicted of a drug felony? (Enter y or n) ")
if criminal_record == "y" or criminal_record == "y":
    eligible_for_financial_aid = False
credit_hours = int(input("How many credit hours are you enrolled next semester?"))
if credit_hours < 6:
    eligible_for_financial_aid = False
gross_yearly_income = int(input("What is your gross yearly income, rounded to the nearest dollar?" "Don't use commas"))
if gross_yearly_income >= 50000:
    eligible_for_financial_aid = False
if eligible_for_financial_aid:
    print("You are eligible to apply for financial aid")
else:
    print("You are not eligible to apply for financial aid")
