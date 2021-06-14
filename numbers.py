def main():
    validate()
    divisible2()
    divisible3()
    divisible5()


def validate():
    num = int(input("Enter a whole number between 20 and 100:"))
    if num in range(20, 101):
        print("This is a valid value!")
    while num < 20 or num > 100:
        print("This is not a valid value")
        num = int(input("Please enter a whole number between 20 and 100:"))


def divisible2():
    for num in range(20, 101):
        if num % 2 == 0:
            print("Number is divisible by 2")
        else:
            print("Number is not divisible by 2 ")


def divisible3():
    for num in range(20, 101):
        if num % 3 == 0:
            print("Number is divisible by 3")
        else:
            print("Number is not divisible by 3")


def divisible5():
    for num in range(20, 101):
        if num % 5 == 0:
            print("Number is divisible by 5")
        else:
            print("Number is not divisible by 5")


main()
