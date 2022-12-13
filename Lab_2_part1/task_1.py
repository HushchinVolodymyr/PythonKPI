
from random import randrange

class Ticket:

    def __init__(self, price, number = 1):
        self.price = price
        self.set_number(number)

    def set_number(self, number):
        number = []
        result = ""
        for el in range(8):
            a = randrange(10)
            number.append(a)
        
        for el in number:
            result = result + str(el)

        self.number = result

        return self.number

    def get_price(self):
        return "Regular price: " + str(self.price)

    def get_number(self):
        return "Number: " + str(self.number)
    

class Advanced_ticket(Ticket):
    
    def __init__(self, price):
        super().__init__(price)

    def andvanced_price(self):
        return "Advanced price: " + str((self.price/100)*60)


class Student_ticket(Ticket):

    def __init__(self, price):
        super().__init__(price)

    def student_price(self):
        return "Student price: " + str((self.price/100)*50)


class Late_ticket(Ticket):

    def __init__(self, price):
        super().__init__(price)

    def late_price(self):
        return "Late price: " + str((self.price/100)*110)


ticket_price = int(input("Enter regular ticket price: "))

regular_ticket = Ticket(ticket_price)
advanced_ticket = Advanced_ticket(ticket_price)
student_ticket = Student_ticket(ticket_price)
late_ticket = Late_ticket(ticket_price)


print(regular_ticket.get_price())
print(regular_ticket.get_number())

print(advanced_ticket.andvanced_price())
print(advanced_ticket.get_number())

print(student_ticket.student_price())
print(student_ticket.get_number())

print(late_ticket.late_price())
print(late_ticket.get_number())
