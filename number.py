def main():
    filename = "sales_error.txt"

    try:
        sales = open(filename, "r")
        record = sales.readline()
        record = record.rstrip('\n')

        while record != "":
            print(record)
            record = sales.readline()
            record = record.rstrip('\n')
            try:
                record = int(record)
            except ValueError:
                print("This value is invalid!")
                print("\t", record)
                break

        sales.close()

    except IOError:
        print("File could not be found")


main()
