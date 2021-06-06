# Operator 	Method
# + 	__add__ (self, other)
# - 	__sub__ (self, other)
# / 	__truediv__ (self, other)
# * 	__mul__ (self, other)
# < 	__lt__ (self, other)
# > 	__gt__ (self, other)
# == 	__eq__ (self, other)



print(5 + 3)  # adding integers using '+'
print("money" + "maker")  # merging strings using '+'

print("\n\nImplementing a complex number class")
class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):  # overloading the `+` operator
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):  # overloading the `-` operator
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp


obj1 = Com(3, 7)
obj2 = Com(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)


print("\n\nMy complex class")
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def printComplex(self):
        print("Real part is ", self.real)
        print("Imaginary part is ", self.imag)

    def __add__(self, other):
        temp = Complex(self.real + other.real, self.imag + other.imag)
        return temp
    
    def __sub__(self, other):
        temp = Complex(self.real - other.real, self.imag - other.imag)
        return temp



# --> 5 + 2i + 2 + 4i 
#     = 7 + 6i
num1 = Complex(5, 2)
num2 = Complex(2, 4)

num3 = num1 + num2   # 7 + 6i
num4 = num1 - num2   # 3 - 2i

num3.printComplex()
num4.printComplex()