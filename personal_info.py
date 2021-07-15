class Personal:
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone


my_info = Personal("Aljeda", "507 Driftwood Ln", "27", "815123456")
friend1 = Personal("Mona", "123 Tall Grass Ln", "28", "815678458")
friend2 = Personal("Andy", "678 Country Brook Ln", "27", "815236890")

print(my_info)
print(friend1)
print(friend2)
