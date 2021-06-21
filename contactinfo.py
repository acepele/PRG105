def main():
    number = int(input("How many people do you want to add to the file? "))
    file = open('myfile.txt', 'w')
    for person in range(0, number):
        name = input("What is the name of the person? ")
        phone = input("What is their phone number? ")
        email = input("What is their email address? ")
        file.write(name + ", " + phone + ", " + email + "\n")
    file.close()


main()
