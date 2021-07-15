def main():
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

    myself = Personal()
    myself.set_name('Aljeda')
    myself.set_address('507 Driftwood Ln')
    myself.set_age('27')
    myself.set_phone('815123456')
    myself.display()

    friend1 = Personal()
    friend1.set_name('Mona')
    friend1.set_address('123 Tall Grass Ln')
    friend1.set_age('28')
    friend1.set_phone('8156599070')
    friend1.display()

    friend2 = Personal()
    friend2.set_name('Andy')
    friend2.set_address('407 Country Brook Ln')
    friend2.set_age('27')
    friend2.set_phone('815797698008')
    friend2.display()


main()
