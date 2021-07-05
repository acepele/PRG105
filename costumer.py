def main():
    list1 = open("accounts.txt", "r")
    list2 = open("over90.txt", "r")
    matches = []
    print("The following accounts are at least 90 days overdue: ")
    for match in list1:
        if list2 in matches:
            matches.append(match)
            print(matches)
    try:
        list1 = open('accounts.txt')
        list1.close()
        list2 = open("over90.txt")
        list2.close()
    except FileNotFoundError:
        print("File cannot be found.")




main()
