class Personal:
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

    def set_address(self, a):
        self.address = a

    def get_address(self):
        return self.address

    def set_age(self, g):
        self.age = g

    def get_age(self):
        return self.age

    def set_phone(self, p):
        self.phone = p

    def get_phone(self):
        return self.phone

    def display(self):
        print("Name: ", self.get_name())
        print("Address: ", self.get_address())
        print("Age: ", self.get_age())
        print("Phone: ", self.get_phone())


def main():
    myself = Personal('Aljeda', '507 Driftwood Ln', '27', '815234567')
    myself.display()

    friend1 = Personal('Mona', '123 Tall Grass Ln', '28', '815123678')
    friend1.display()

    friend2 = Personal('Andy', '789 Country Brook Ln', '27', '815999646')
    friend2.display()


main()
