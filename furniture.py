class OfficeFurniture:
    def __init__(self, category, material, quantity, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__quantity = quantity
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_quantity(self):
        return self.__quantity

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_item_price(self):
        return self.__price * self.__quantity

    def str(self):
        item = self.__category + "qty-" + str(self.__quantity) + " each: $(:0,.2f)".format(self.__price) + \
               " total = $(:0,.2f)".format(self.get_item_price())
        return item


class Desk(OfficeFurniture):
    def __init__(self, category, material, quantity, length, width, height, price, location_of_drawers, number_drawers):
        OfficeFurniture.__init__(self, category, material, quantity, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    def str(self):
        printline = "Product: " + self.get_location_of_drawers() + "Drawers: " + self.get_number_drawers() + \
                    "qty-" + str(self.__quantity) + " each: $(:0,.2f)".format(self.__price) + \
               " total = $(:0,.2f)".format(self.get_item_price())
        return printline
