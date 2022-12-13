class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator

    def set_numerator(self, numerator, denominator):
        minim = min(numerator, denominator)
        nod = 1

        for el in range(1, minim + 1):
            if numerator % el == 0 and denominator % el == 0:
                nod = el

        self.numerator = numerator / nod

    def set_denominator(self, numerator,  denominator):
        if  denominator != 0:
            minim = min(numerator, denominator)
            nod = 1

            for el in range(1, minim + 1):
                if numerator % el == 0 and denominator % el == 0:
                    nod = el
            self.denominator = denominator / nod
        else:
            print("Can`t divide on zero! set to default value 1!")

    def adding_numbers(self):
        return self.numerator + self.denominator

    def subtracting_numbers(self):
        return self.numerator - self.denominator

    def multiplying_numbers(self):
        return self.numerator * self.denominator

    def devide_nummbers(self):
        if denominator != 0:
            return self.numerator / self.denominator
        else:
            return "Can`t divide on zero!"

    def comprasion_numbers(self):
        if self.numerator > self.denominator:
            return "Numerator more than denominator"
        elif self.numerator == self.denominator:
            return "Numerator equal denominator"
        elif self.numerator < self.denominator:
            return "Numerator less then denominator"
        else:
            return "Not correct data!"

    def fractional_var(self, numerator, denominator):
        return str(self.numerator) + "/" + str(self.denominator)

    def decimal_var(self, numerator, denominator):
        return (self.numerator / self.denominator)

fraction = Rational()

numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

fraction.set_numerator(numerator, denominator)
fraction.set_denominator(numerator, denominator)

choisse = int(input("Choisse:\n 1. Adding numbers.\n 2. Subtracting number.\n 3. Multiplying numbers.\n 4. Devide numbers.\n 5. Comprasion numbbers.\n 6. Fraction.\nEnter your choise: "))

if str(choisse) in "1, 2, 3, 4, 5, 6":
    if choisse == 1:
        print("Adding numers: ", fraction.adding_numbers())
    elif choisse == 2: 
        print("Subtracting nubers: ", fraction.subtracting_numbers())
    elif choisse == 3:
        print("Multiplying numbers: ", fraction.multiplying_numbers())
    elif choisse == 4:
        print("Divide numbers: ", fraction.devide_nummbers())
    elif choisse == 5:
        print("Comprasion numbers: ", fraction.comprasion_numbers())
    elif choisse == 6:
        print("Fractional variant: ", fraction.fractional_var(numerator, denominator))
        print("Decimal variant: ",fraction.decimal_var(numerator, denominator))
else:
    print("Not such varint")
