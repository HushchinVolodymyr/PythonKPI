class Product:
    def __init__(self, price = 0, description = "", dimension = ""):
        self.price = price
        self.description = description
        self.dimension = dimension

    def set_price(self, price):
        self.price = price

    def set_description(self, description):
        self.description = description

    def set_dimension(self, dimension):
        self.dimension = dimension

    def full_inf(self):
        return "Car price: " + str(self.price) + " Car description: " + self.description + " Car dimension: " + self.dimension

class Customer:
    def __init__(self, surname = "", name = "", patronymic = "", phone = ""):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone = phone

    def set_full_name(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def set_phone(self, phone):
        self.phone = phone

    def get_customer_inf(self):
        return self.surname + " " + self.name + " " + self.patronymic + " Number: " + str(self.phone)


class Order():
    def __init__(self,customer, products, price):
        self.customer = customer
        self.products = products
        self.price = price

    def count_price(self):
        total_price = 0
        for el in self.products:
            total_price += el.price
        return total_price
