class Lamp:
    def __init__(self):
        self.c=0
        self.l= ['Green', 'Red', 'Blue', 'Yellow']
    def light(self):
        self.s=self.l[self.c%4]
        self.c+=1
        return self.s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    print(lamp_1.light()) #Green
    print(lamp_1.light()) #Red
    # print(lamp_1.light()) 
    # print(lamp_1.light()) 
    # print(lamp_1.light()) 
    print(lamp_2.light()) #Green
    
    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")