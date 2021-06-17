


def main():
    print("This program will find the area of a shape for you.")
    menu = 0
    while menu < 1 or menu > 5:
        print(" 1.Rectangle\n 2.Triangle\n 3.Square\n 4.Circle\n 5.Quit")
        menu = int(input("Please enter the number of your selection: "))
        if menu > 4:
            print("That is not a valid number")
        else:
            print("You picked " + str(menu))

    if menu == 1:
        w = float(input("Please enter the width of the rectangle in cm: "))
        h = float(input("Please enter the height of the rectangle in cm: "))
        area_of_rectangle(w, h)

    elif menu == 2:
        b = float(input("Enter the base of the triangle in cm: "))
        c = float(input("Enter the height of the triangle in cm:"))
        area_of_triangle(b, c)

    elif menu == 3:
        side = float(input("Enter the side of the square in cm: "))
        area_of_square(side)

    elif menu == 4:
        r = float(input("Please enter the length of the radius of the circle: "))
        area_of_circle(r)
    else:
        print("Quit!")


def area_of_rectangle(width, height):
    area = width * height
    print("\n Area of a Rectangle is: %.2f" % area)


def area_of_triangle(b, c):
    area = (b * c) / 2
    print("\n Area of a Triangle is: %.2f" % area)


def area_of_square(side):
    area = side * side
    print("\n Area of a Square is: %.2f" % area)


def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    print("\n Area of a Circle is: %.2f" % area)


main()
