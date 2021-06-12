def main():
    print("Select one of the menu options below to find out more:")
    print("1. Mediterranean sandwich ")
    print("2. Pasta salad")
    print("3. Beef burger")
    print("4. Gyro")
    print("5. Stuffed peppers")
    selection = int(input("Please enter the number of your choice: "))
    if selection == 1:
        mediterranean()
    elif selection == 2:
        pasta()
    elif selection == 3:
        beef()
    elif selection == 4:
        gyro()
    elif selection == 5:
        peppers()


def mediterranean():
    print("Zippy hummus and feta cheese toasted")
    print("and them topped with artichoke hearts")


def pasta():
    print("Pasta salad is a salad dish prepared with one or more type of pasta")
    print("and most often tossed in a vinegar, oil or mayonnaise-based dressing")


def beef():
    print("Combine ground beef,pepper,salt,mustard and Worcestershire sauce")


def gyro():
    print("This greek chicken gyro uses fresh marinated chicken and then stuffed into a warm pita")
    print("and topped with homemade tzatziki, tomato, onion, lettuce and fresh dill")


def peppers():
    print("Peppers filled with any of a variety of fillings,including meat,vegetables,cheese,rice or sauce")


main()
