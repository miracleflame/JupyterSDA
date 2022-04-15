class Rectangle:
    # když se vytvoří reclangle objekt bude brát input délku a výšku stran (width, height)
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle - libovoly text"

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        return self.height * (self.width * "*" + "\n")

class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        super().__init__(length, length)

    def __str__(self):
        return f"Ctverec se stranou {self.length}."

    def set_side(self, new_lenght):
        self.length = new_lenght

square = Square(4)
print(square)
print(square.get_picture())