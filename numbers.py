def main():
    number = int(input("Enter a whole number between 20 and 100: "))
    good_number = validate(number)
    divisible_by_two(good_number)
    divisible_by_three(good_number)
    divisible_by_five(good_number)
    output(good_number, two, three, five)


def validate(num):
    if 20 <= num <= 100:
        return num
    else:
        while num < 20 or num > 100:
            print("This is not a valid value")
            num = int(input("Please enter a whole number between 20 and 100:"))
        return num


def divisible_by_two(num):
    if num % 2 == 0:
        print("Number is divisible by 2")
    else:
        print("Number is not divisible by 2 ")


def divisible_by_three(num):
    if num % 3 == 0:
        print("Number is divisible by 3")
    else:
        print("Number is not divisible by 3")


def divisible_by_five(num):
    if num % 5 == 0:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")


def output(num, two_div, three_div, five_div):
    print(str(num) + two_div)
    print(str(num) + three_div)
    print(str(num) + five_div)


main()
