def main():
    language = {'one': 'nje', 'two': 'dy', 'three': 'tre', 'four': 'kater', 'five': 'pese',
                'six': 'gjashte', 'seven': 'shtate', 'eight': 'tete', 'nine': 'nente', 'ten': 'dhjete'}
    print("QUIZ \n")
    number = int(input("Enter the number in English which corresponds to the number in Albanian: "))
    print("\nYou got {1}.".format(number, quiz(language), len(language)))


def quiz(language):
    score = 0
    for number in language.item():
        if input(number).lower() == number.lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect")


main()
