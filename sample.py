def main():
    sales = open("sales_totals", "r")
    lines = sales.readlines()
    lines = lines.rstrip("\n")
    count = 0
    total = 0
    output()


for line in sales:
    print(line)
    total += int(line)
    count = count + 1
    print("The sum is:", total)


def output():
    print("Total: ", format(total))
    print("Number of entries: ", format(count))
    print("Average: ", format(average))


    sales.close()


main()
