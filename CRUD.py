import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        import_file = open("costumer_file.dat", 'rb')
        costumers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        print("file not found, please add a costumer and the quit to create the file")
        costumers = {}

    choice = 0

    while choice != QUIT:
        choice = menu

        if choice == LOOK_UP:
            look_up(costumers)
        elif choice == ADD:
            add(costumers)
        elif choice == CHANGE:
            change(costumers)
        elif choice == DELETE:
            delete(costumers)
        elif choice == QUIT:
            save(costumers)


def menu():
    print()
    print("Costumer phone lookup")
    print("""""""""""""""""""")
    print("1. Look up a costumer")
    print("2. Add a new costumer")
    print("3. Change a phone number")
    print("4. Delete a costumer")
    print("5. Quit the program\n")
    choice = int(input("Enter the number of your choice: "))
    while choice < 1 or choice > 5:
        choice = int(input("Enter a valid choice: "))
    return choice


def look_up(costumers):
    name = input("Enter a costumer name: ")
    print(costumers.get(name, "Not Found"))


def add(costumers):
    name = input("Enter costumer name: ")
    phone = input("Enter costumer phone number: ")
    if name not in costumers:
        costumers[name] = phone
    else:
        print("That entry already exists.")


def change(costumers):
    name = input("Enter costumer name: ")
    if name in costumers:
        phone = input("Enter the new phone number: ")
        costumers[name] = phone
    else:
        print("That costumer is not found")


def delete(costumers):
    name = input("Enter costumer name: ")
    if name in costumers:
        del costumers[name]
    else:
        print("That costumer is not found")


def save(costumers):
    print("The data file has been updated with your changes ")
    save_file = open("costumer_file.dat", 'wb')
    pickle.dump(costumers, save_file)
    save_file.close()


main()
