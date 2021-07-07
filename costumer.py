def main():
    try:
        list1 = open('accounts.txt')
        accounts = list1.readlines()
        list1.close()
        list2 = open("over90.txt")
        over90 = list2.readlines()
        list2.close()
        print("The following accounts are at least 90 days overdue: ")
        for over in over90:
            over = over.strip("\n")
            for account in accounts:
                if over in account:
                    print(account)
    except FileNotFoundError:
        print("File cannot be found.")


main()
