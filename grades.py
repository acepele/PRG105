def main():
    outfile = open("grades.txt", "w")
    for line in grades:
        lineout = "'" + line[0] + "', '" + line[1] + "'\n"
        outfile.writelines(lineout)
    outfile.close()

    len_list = int(input("How many students do you need to enter grades for?"))
    list1 = []  # created an empty list
    for i in range(len_list):
        name = input("Enter the name of student: ")
        list1.append(name)
        print(list1)
    for i in range(len_list):
        grades = input("Enter the student's final letter grade: ")
        list1.append(grades)
        print(list1)




main()
