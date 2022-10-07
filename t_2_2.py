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

    def fractional_var(self, numerator, denominator):
        return str(self.numerator) + "/" + str(self.denominator)

    def decimal_var(self, numerator, denominator):
        return (self.numerator / self.denominator)

fraction = Rational()

numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

fraction.set_numerator(numerator, denominator)
fraction.set_denominator(numerator, denominator)

print("Fractional variant: ", fraction.fractional_var(numerator, denominator))
print("Decimal variant: ",fraction.decimal_var(numerator, denominator))
