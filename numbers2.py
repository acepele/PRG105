import math

PI = 3.14


def main():
    print("This program will find the area of a shape for you.")
    menu = 0
    while menu < 5:
        print(" 1.Rectangle\n 2.Triangle\n 3.Square\n 4.Circle\n 5.Quit")
        menu = int(input("Please enter the number of your selection: "))
        if menu > 4:
            print("That is not a valid number")
        else:
            print("You picked " + str(menu))


def area_of_rectangle(width, height):
    width = float(input("Enter the width of the rectangle in cm: "))
    height = float(input("Enter the height of the rectangle in cm:"))
    area = width * height
    print("\n Area of a Rectangle is: %.2f" % area)


def area_of_triangle(a, b, c):
    b = float(input("Enter the base of the triangle in cm: "))
    c = float(input("Enter the height of the triangle in cm:"))
    area = (a + b + c) / 2
    print("\n Area of a Triangle is: %.2f" % area)


def area_of_square(side):
    area = side * side
    print("\n Area of a Square is: %.2f" % area)


def area_of_circle(pi, r):
    radius = float(input("Please enter the length of the radius of the circle:"))
    area = PI * r * r
    print("\n Area of a Circle is: %.2f" % area)


main()
