# Operator Overloading in Python

#%%
# Overloading of "+" operator

print(1 + 2)

print("My name is " + "Anmol Arora")

#%%
# Overloading of "*" operator

print(3 * 4)

print("Anmol" * 4)

#%%
# Overload a binary "+" operator

class A:
    def __init__(self, a):
        self.a = a
        
    def __add__(self, o):
        return self.a + o.a
    
ob1 = A(1)
ob2 = A(2)

ob3 = A("Anmol")
ob4 = A("Arora")

print(ob1 + ob2)
print(ob3 + ob4)

#%%
# Addition of two complex numbers
# using binary "+" operator overloading

class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
    
    def __str__(self):
        return self.a, self.b
    
ob1 = complex(1, 2)
ob2 = complex(2, 3)
ob3 = ob1 + ob2
print(ob3)

#%%
# Overload comparison operators
# and equality operator

class A:
    def __init__(self, a):
        self.a = a
        
    def __gt__(self, other):
        if(self.a > other.a):
            return True
        else:
            return False
        
    def __lt__(self, other):
        if(self.a < other.a):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if(self.a == other.a):
            return True
        else:
            return False
        

ob1 = A(3)
ob2 = A(6)
ob3 = A(1)
ob4 = A(9)
ob5 = A(6)
ob6 = A(1)

if(ob1 > ob3):
    print('ob1 is greater than ob3')
else:
    print('ob3 is greater than ob1')
    
if(ob2 < ob4):
    print('ob2 is less than ob4')
else:
    print('ob4 is less than ob2')
    
if(ob2 == ob6):
    print('Both are equal')
else:
    print('Both are not equal')