import question
import random


def main():
    q1 = question.Question("Hg is the chemical symbol of which element? ", "A.Helium", "B.Magnesium",
                           "C.Mercury", "D.Hassium", "C")
    q2 = question.Question("What is the capital city of Spain? ", "A.Madrid", "B.Paris", "C.Athina",
                           "D.Roma", "A")
    q3 = question.Question("What is the third sign of the zodiac? ", "A.Virgo", "B.Scorpio",
                           "C.Aquarius", "D.Gemini", "D")
    q4 = question.Question("Which country invented tea? ", "A.Brazil", "B.Greece", "C.China",
                           "D.France", "C")
    q5 = question.Question("What language has the most words? ", "A.English", "B.French",
                           "C.Italian", "D.Albanian", "A")
    q6 = question.Question("How many phases of the moon are there? ", "A.2", "B.4", "C.6", "D.8", "D")
    q7 = question.Question("Which sport does Costantino Rocca play? ", "A.Basketball", "B.Football",
                           "C.Golf", "D.Volleyball", "C")
    q8 = question.Question("What year did the Titanic movie come out? ", "A.1995", "B.1997", "C.1998",
                           "D.1999", "B")
    q9 = question.Question("How many hearts does an octopus have? ", "A.1", "B.2", "C.3", "D.4", "C")
    q10 = question.Question("What color is a Himalayan poppy flower? ", "A.Blue", "B.Pink", "C.Purple",
                            "D.Yellow", "A")


    all_the_question = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    print("***Player One***")
    player_1 = ask(all_the_question)
    print("***Player two***")
    player_2 = ask(all_the_question)

    if player_1 == player_2:
        print("It is a tie!")
    elif player_1 > player_2:
        print("Player One is the winner!")
    else:
        print("Player Two is the winner")


    def ask(all_questions):
        correct = 0
        for item in range(2):
            player_questions = random.choice(all_questions)
            print(player_questions.get_question())
            print("A. " + player_question.get_a1())
            print("B. " + player_question.get_a2())
            print("C. " + player_question.get_a3())
            print("D. " + player_question.get_a4())
            player_response = input("Please enter the letter of your answer: ")

            if player_response.upper() == player_questions.get_correct_answer():
                print("\nWhoopee! You got the one\n\n")
                correct += 1
            else:
                print("\nSo sad.Better luck next time.\n\n")

        return correct


main()
