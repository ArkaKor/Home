class Adress:
    index = 111111
    city = "Город"
    street = "Улица"
    house = 23
    flat = 65

    def __init__(self, index, city, steet, house, flat):
        self.i = index
        self.c = city
        self.s = steet
        self.h = house
        self.f = flat
    
    def __str__(self):
        return f"{self.i}, {self.c}, {self.s}, {self.h} - {self.f}"
