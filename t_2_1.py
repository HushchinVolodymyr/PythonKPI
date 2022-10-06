class Rectangle:

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        if isinstance(length, int) or isinstance(length, float):
            if 0 < int(length) < 20:
                self.length = length
            else:
                print("Length must be between 0 and 20")
        else:
            print("Length must be number!")

    def get_width(self):
        return self.width

    def set_width(self, width):
        if isinstance(width, int) or isinstance(width, float):
            if 0 < int(width) < 20:
                self.width = width
            else:
                print("Width must be between 0 and 20")
        else:
            print("Width must be number!")

    def perimetr(self, width, length):
        return ((self.width + self.length) * 2)

    def area(self, width, length):
        return self.width * self.length


rectangle1 = Rectangle()

length = int(input("Length "))
width = int(input("Width "))

rectangle1.set_length(length)
rectangle1.set_width(width)

print("Perimetr:", rectangle1.perimetr(length, width))
print("Area:", rectangle1.area(length, width))
