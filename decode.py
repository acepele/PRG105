def main():
    secret_code = ['0', 'h', '!', '_', 'f', '!', '#', '!', '$', '&', '#', 'k', 'h', '_', '*', 'k',
                   '}', '!', '^', '#', 'm', '!', '_', ';', '!', 'h', ')', '&', '!', ';', '&', '_',
                   '(', ')', '$', ',', 's', ')', ',', ',', '^']

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'X', 'Y', 'Z', '', ',', '.', '!', '?']

    outline = []
    print("This program will decode a coded text file.")
    filename = input("What is the name of the file to decode? ")
    for line in filename:
        try:
            outfile = open("secret_code.txt", 'r')
            for secret_code in outfile.readlines():
                print(secret_code)
        except ValueError:
            print("File cannot be found")

            outfile = open("secret_code.txt", 'r')
            for item in outline:



        outfile.close()



main()
