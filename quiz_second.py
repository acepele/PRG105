class Question:
    def __init__(self, question, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__a5 = a5
        self.__a6 = a6
        self.__a7 = a7
        self.__a8 = a8
        self.__a9 = a9
        self.__a10 = a10
        self.__answer = answer

    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_a5(self, a5):
        self.__a5 = a5

    def set_a6(self, a6):
        self.__a6 = a6

    def set_a7(self, a7):
        self.__a7 = a7

    def set_a8(self, a8):
        self.__a8 = a8

    def set_a9(self, a9):
        self.__a9 = a9

    def set_a10(self, a10):
        self.__a10 = a10

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_a5(self):
        return self.__a5

    def get_a6(self):
        return self.__a6

    def get_a7(self):
        return self.__a7

    def get_a8(self):
        return self.__a8

    def get_a9(self):
        return self.__a9

    def get_a10(self):
        return self.__a10

    def get_answer(self):
        return self.__answer
