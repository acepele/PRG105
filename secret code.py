def main():
    secret_code = ['0', 'h', '!', '_', 'f', '!', '#', '!', '$', '&', '#', 'k', 'h', '_', '*', 'k',
                   '}', '!', '^', '#', 'm', '!', '_', ';', '!', 'h', ')', '&', '!', ';', '&', '_',
                   '(', ')', '$', ',', 's', ')', ',', ',', '^']

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'X', 'Y', 'Z', '', ',', '.', '!', '?']

    message = input("Please enter the message you want converted into code: ")

    filename = open("secret_code.txt", 'w')
    secret_code_final = ""
    for letter in message:
        for item in range(0, len(alphabet)):
            if letter.upper() == alphabet[item]:
                secret_code_final += (secret_code[item] + " ")
                filename.writelines(secret_code)

    print(secret_code_final)
    filename.close()


main()
