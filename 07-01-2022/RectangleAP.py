class Rectangle:
    def __init__(self,l,b):
        self.a1 = l
        self.b1 = b
    def disp(self):
        self.s = self.a1 * self.b1
        print("Area of the Rectangle:",self.s)
        self.su=2*(self.a1 + self.b1)
        print("Perimeter of the Rectangle:", self.su)
        return self.s
    def comp(self,rect1):
        if(self.s==rect1.s):
            print("Area of both rectangles are equal")
        else:
            print("Area of both rectangles are not equal")
l = int(input("Enter the length of 1st Rectangle: "))
b = int(input("Enter the breadth of 1st Rectangle: "))
rect = Rectangle(l,b)
h = int(input("Enter the length of 2nd Rectangle: "))
m = int(input("Enter the breadth of 2nd Rectangle: "))
rect1 = Rectangle(h,m)
rect.disp()
rect1.disp()
rect.comp(rect1)


