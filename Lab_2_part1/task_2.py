

class Pizza:
    def __init__(self): 
        self.compound = ["dought", "souce", "sosuges", "peper"]
       
    def add_ingredient(self, extra_ingr):
        if extra_ingr in "Mashroom, Cheese":
            self.compound.append(extra_ingr.add_to_pizza())
        else:
            print("Not such extra ingredient in meny!")

    def __str__(self):
        return self.name + " for " + str(self.pizza_price)


class extra_ingr:
    def __init__(self) -> None:
        pass

    def add_to_pizza(self):
        return self.name

class Mashroom(extra_ingr):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Mashroom"

class Cheese(extra_ingr):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Cheese"


class Margarita(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_price = 100
        self.name = "Margarita"

class Four_cheese(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_price = 110
        self.name = "Four_cheese"

class Hawaii(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_price = 105
        self.name = "Hawaii"

class Vegan(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_price = 140
        self.name = "Vegan"

class Peperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_price = 100
        self.name = "Peperoni"

class Carbonara(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_price = 120
        self.name = "Carbonara"

class Meat(Pizza):
    def __init__(self):
        super().__init__()
        self.pizza_price = 130
        self.name = "Meat"

def Pizza_of_day(date):
    if date in "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday":
        if date in "Monday":
            return Margarita()
        elif date in "Tuesday":
            return Four_cheese()
        elif date in "Wednesday":
            return Hawaii()
        elif date in "Thursday":
            return Vegan()
        elif date in "Friday":
            return Peperoni()
        elif date in "Saturday":
            return Carbonara()
        elif date in "Sunday":
            return Meat()
    else:
        print("Not correct day of week!")
   
margarita = Margarita()
four_cheese = Four_cheese()
hawaii = Hawaii()
vegan = Vegan()
pepeorni = Peperoni()
carbonara = Carbonara()
meat = Meat()

date = str(input("Enter day of week: "))
print("Today specail offer:", Pizza_of_day(date))

