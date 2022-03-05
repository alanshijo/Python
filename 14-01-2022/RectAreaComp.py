class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
        self.area=self.l * self.b
    def __lt__(self, other):
        if self.area < other.area:
            print("Not equal")
        elif other.area < self.area:
            print("Not equal")
        else:
            print("They have equal area")
l = int(input("Enter length of first rectangle: "))
b = int(input("Enter breadth of first rectangle: "))
R1 = Rectangle(l,b)
l = int(input("Enter length of second rectangle: "))
b = int(input("Enter breadth of second rectangle: "))
R2 = Rectangle(l,b)
R1 < R2