a=2
b=3
c=10

sum_all = a+b+c
new_value = sum_all/10

print(new_value)


#This is a comment
print('Hello world')

"""
comment in more than one line
"""

my_list = [1, 2, 3]
my_cut_list = my_list[0:1]
print(my_cut_list)

A = [1, 2, 3]
#deep copy
C = A[:]
#shallow copy
B = A
B[0] = 9
print(B)
print(A)
print(C)

#Flow Control: if, elif, else
num = 1
if num > 0:
    print('Positive')
elif num == 0:
    print('Zero')
else:
    print('Negative')
    
    
#num = float(input('Enter a number')

"""
For loop
1,For each
    for value in my_list:
        sum += sum
2,For range
    for i in range(len(my_list)):
        print(my_list[i])
3, For loop with else:
"""
my_numbers = [0, 1, 2]
for i in my_numbers:
    print(i)
else:
    print('No more iterms.')
    
#while loop
i = 1
while i < 100:
    print(i**2)
    i += i**2
    
#Functions
#A group of statements to perform a specific task
def greet(name):
    print('Hello,' + name +'. Good morning!')
    
def send_email(to, subject, content):
    #some code to send email
    return True

if(send_email('test@test.com', 'Hello Test', 'this is a sample email')):
    print('email sent')
else:
    print('email failed')

greet('wang')

"""
More on GitHub
Push
Pull Request
Pull
"""

"""
Variable Scope
Global variables
Local variables
"""

"""
OOP
Objects:
attributes/actions
An objtct(instance) is an instantiation of a class
"""

#Class
class Vehicle:
    #class attribute
    type = 'sedan'
    #instance attribute
    def __init__(self, production_year, make):
        self.production_year = production_year
        self.make = make
        
#instantiate the Parrot class
model_3 = Vehicle('2020', 'Tesla')
model_e = Vehicle('1990', 'Benz')

#access the class attributes
print(model_3.__class__.type)

print(model_3.production_year)

"""
inheriatance
class Vehicle:
    def __init__(self):
        print('Vehicle is ready")
        
    def who_is_this(self):
        print('Vehicle')
        
    
class Truck(Vehicle):
    def __init__(self):
    #call super() function
        super().__init__()
        
    def who_is_this(self):
        print('Truck')
    ...
"""
    
#Encapsulation
class Computer:
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print(self.__maxprice)
        
    def setMaxPrice(self, price):
        self.__maxprice = price
        
c = Computer()
c.sell()
#change the price
c.__maxprice = 1000
c.sell()
#using setter function
c.setMaxPrice(1000)
c.sell()


#Polymorphism
class Parrot:
    
    def fly(self):
        print('Parrot can fly')
    def swim(self):
        print('Parrot cannot swim')
        
class Penguin:
    
    def fly(self):
        print('Penguin cannot fly')
    def swim(self):
        print('Penguin can swim')
        
def flying_test(bird):
    bird.fly()
    