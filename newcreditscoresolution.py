credit_score = int(input("What is your credit score? "))
if credit_score >= 720:
    print("Your credit is excellent!")
elif credit_score >= 690:
    print("Your credit is good.")
elif credit_score > 630:
    print("Your credit is fair.")
else:
    print("Your credit is bad.")
