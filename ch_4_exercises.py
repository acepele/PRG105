"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 4.2 A condition controlled loop
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0: while num > 0
num = 10
# write your code here, the variable needs to exist before you start the loop

number = 10
while number >= 0:
    print(number)
    number = number - 1


# TODO 4.3 the For Loop
print("=" * 10, "Section 4.3 for loop", "=" * 10)
# Use a for loop with a list of the days of the week,
# print each day of the week

for days_of_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
    print(days_of_week)

# TODO 4.3 the for loop - range function
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
# use the range function to print the numbers from 1 to 10
print("\n\nrange(1, 10)")
for number in range(1, 11):
    print(number)


# TODO 4.4 a running total
print("=" * 10, "Section 4.4 running total", "=" * 10)
# Use a loop to have the user enter 5 numbers, provide a total at the end
# You will need to initialize your accumulator before entering the loop
# You can assume valid integers are entered
total = 0
number1 = int(input('Please enter the first number: '))
number2 = int(input('Please enter the second number: '))
number3 = int(input('Please enter the third number: '))
number4 = int(input('Please enter the fourth number: '))
number5 = int(input('Please enter the fifth number: '))
for num in range(1, number5):
    total = number1 + number2 + number3 + number4 + number5
print("Total sum of the numbers entered is ", +total)

# TODO 4.5 Sentinel Value
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Use a loop to have the user enter test scores until a
# sentinel value of -1 is entered.
# After the loop, display the total, the count and the average (total / count)

count = 0
total_amt = 0
test_score = 0
print("Enter test scores. Enter -1 when you are done")
while test_score >= 0:
    test_score = float(input("Enter the next test score: "))
    if test_score >= 0:
        total_amt += test_score
        count += 1
average = total_amt / count
print(format(average, '.2f') + 'is the average of the ' + str(count) + ' test score you entered')

# TODO 4.6 validating data
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data

number = int(input("Enter a number from 1 to 10: "))
while number < 1 or number > 10:
    print("Error: The number cannot be negative or greater than 10")
    number = int(input("Enter the correct number from the range 1 to 10: "))
print("Program continues...")
