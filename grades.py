def main():
    line = []
    student_grades = []
    len_list = int(input("How many students do you need to enter grades for?"))
    for student in range(0, len_list):
        name = input("Enter the name of student " + str(student + 1) + ": ")
        grades = input("Enter the student's final letter grade: ")
        line.append(name)
        line.append(grades)
        student_grades.append(line)
        line = []
    print(student_grades)

    outfile = open("grades.txt", "w")
    for line in student_grades:
        lineout = "'" + line[0] + "', '" + line[1] + "'\n"
        outfile.writelines(lineout)
    outfile.close()


main()
