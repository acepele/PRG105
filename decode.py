def main():
    secret_code = ['z', 'r', 's', '@', '2', '3', '4', '5', '6', '7', '8',
                   '9', '0', '-', '=', '+', ';', '?', '>', '.', 'm', 'n',
                   'b', 'v', 'z', ' ', 'a', 's', 'd', 'f', 'g']

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'X', 'Y', 'Z', '', ',', '.', '!', '?', ' ']

    print("This program will decode a coded text file.")
    filename = input("What is the name of the file to decode? ")
    solution = ""
    outline = []

    try:
        outfile = open(filename, 'r')
        outline = outfile.readlines()
        outfile.close()
    except ValueError:
        print("File cannot be found")
    for item in outline:
        item = item.strip('\n')
        if item in secret_code:
            my_index = secret_code.index(item)
            solution += alphabet[my_index]

    print(solution)


main()
