class Rectangle:
    x = 0
    y = 0
    def set(self):
        self.x = eval(input("enter the value of side1(x):"))
        self.y = eval(input("enter the value of side2(y):"))
    def get(self):
        print(f"value of side 1 is:{self.x}")
        print(f"value of side 2 is:{self.y}")
    def area(self):
        print("area of reactangle is:",self.x*self.y)

class Circle(Rectangle):
    radius = 0
    def get(self):
        self.radius = eval(input("enter the radius:"))
    def area(self):
        print(f"area of the circle is: {(22/7)*pow(self.radius,2)}")

R = Rectangle()
R.set()
R.get()
R.area()
C = Circle()
C.get()
C.area()