def main():
    file = open('myfile.txt', 'w')
    number = input("How many people do you want to add to the file? ")
    name = input("What is the name of the person? ")
    phone = input("What is their phone number? ")
    email = input("What is their email address? ")

    file.write(number + "\n")
    file.write(name + "\n")
    file.write(phone + "\n")
    file.write(email + "\n")




file.close()

main()
