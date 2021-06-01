credit_score = int(input("What is your credit score? "))
if 300 < credit_score < 629:
    print("Your credit score is bad")
elif 630 < credit_score < 689:
    print("Your credit score is fair")
elif 690 < credit_score < 719:
    print("Your credit score is good")
else:
    print("Your credit score is excellent")
