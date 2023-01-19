#A = { 55, 6, 8, 9, 11} , B = {44, 55, 89,54} apply set union.

#Method 1

Kallol = {1 ,2 , 3 , 4}
Hussain = {5 , 6 , 7, 8}

Sovle = Kallol.union(Hussain)
print(Sovle)

#Method 2

Kallol = {1 ,2 , 3 , 4}
Hussain = {5 , 6 , 7, 8}

Sovle = Kallol | Hussain
print(Sovle)

#Which data type not allow duplicate item. Give an example.

Kl = {1, 2 , 3}
Kl.add(4)
Kl.add(2) #Will Not Inclued This
print(Kl)

#B={‘Django’: 16, ‘Project’: 8, ‘Students’: 20} print keys.

#Method 1

B={"Django": 16, "Project": 8, "Students": 20}
Kallol = B.keys()
print(Kallol)

#Method 2

B={"Django": 16, "Project": 8, "Students": 20}
for kl27 in B:
    print(kl27)

#Create a function & call the function.

#Method 1

def kallol(Age):
    print('Kallol is ' + Age + " Old.")
kallol("26 Years" + " 4 Months")

#Method 2

def kallol27 (a , b):
    return (a + b)
Shakib = kallol27(30 ,40)
print(Shakib)

#Create Class & Object.

class My_kallol:
    def __init__(Check, name, age):
        Check.name = name
        Check.age = age

    def Call(Check):
        print("Hi, This is " + Check.name + " and I am " + str(Check.age) + " years old.")
Details = My_kallol("Kallol Hossain", 26)
Details.Call()

#Give an example of Inheritance.

class Parent:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name:", self.name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def display(self):
        super().display()
        print("Age:", self.age)

c = Child("Kallol", 26)
c.display()



