class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.so = south
        self.we = west
        self.wi = width_WE
        self.le = width_NS
        self.he = height

        self.cor= {'north-east': [self.so+self.le,self.we+self.wi], 
                        'south-east': [self.so, self.we+self.wi],
                        'south-west': [self.so, self.we], 
                        'north-west': [self.so+self.le,self.we]  }


        

    def corners(self):
        return self.cor

    def area(self):
        return self.wi * self.le

    def volume(self):
        return self.area() * self.he

    def __repr__(self):
        return "Building("+ str(self.so)+", "+str(self.we)+", "+str(self.wi) + ", "+str(self.le)+", "+str(self.he)+")"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    print(b)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
