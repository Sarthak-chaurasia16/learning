#Class Variables
class Car:
    Total_car = 0

    def __init__(self ,brand , model):
        self.__brand = brand
        self.model = model
        Car.Total_car +=1 
    def fuel_type(self):
        return "Petrol And Deisel"
    def get_brand(self):
        return self.full_name() 
    def full_name(self):
        return f"{self.model} by {self.__brand}"

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__( brand , model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    
#Electric_1 = ElectricCar("Tesla", "Model S", "90KWh")
car1 = Car("Tata", "Safari")
car2 = Car("Bentley","Flying Spur")
#Class variable hai total car isliye direct access le skte hai class se
print(Car.Total_car)
print("Exit Successfully:)")


#Static Method
#Add a static method to the car class that returns a general description of a car
class Car:
    def __init__(self ,brand , model):
        self.__brand = brand
        self.model = model 
    def fuel_type(self):
        return "Petrol And Deisel"
    def get_brand(self):
        return self.full_name() 
    def full_name(self):
        return f"{self.model} by {self.__brand}"
    @staticmethod
    def general_description():
        return "Car is a means of transport"

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__( brand , model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
#Static method use krne se hume function mein self nhi likhna padega kuki uski line hi nhi jodni hai 
#kuki object access nhi kr skta hai uss function ko sirf class mein accessible hai ye function
my_car1 = Car("Tata", "Safari")
#print(my_car1.general_description())
print(Car.general_description())
exit
print("Exit Successfully:)")

#Property Decorators
# Question mein bola hai property ko read only mein convert karo
#Abhi tak ho ye raha hai ki koi bhi property ko hum abhi overwrite kar skte hai like my_car1.model = "City"
# krenge toh ye overwrite ho kar safari ke jagah city likh dega isliye hume convert krna padega  
class Car:
    Total_car = 0

    def __init__(self ,brand , model):
        self.__brand = brand
        self.__model = model
        Car.Total_car +=1 
    def fuel_type(self):
        return "Petrol And Deisel"
    def get_brand(self):
        return self.full_name() 
    def full_name(self):
        return f"{self.__model} by {self.__brand}"
      #Private ho gya hai model toh ab class ke bahar access nhi ho skta directly toh ab menthod bana hoga 
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__( brand , model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    
my_car = Car("Tata", "Safari")
#my_car.model ="city" # Property ki wajah se overwrite nhi hoga ab
#car2 = Car("Bentley","Flying Spur")
# Hamare decorator ne use ek property ki tarah access krne ke liye de dia hai isliye parenthesis nhi lagana padega
print(my_car.model)
print("Exit Successfully:)")
# Class inheritance and isinstance() function
class Car:
    Total_car = 0

    def __init__(self ,brand , model):
        self.__brand = brand
        self.__model = model
        Car.Total_car +=1 
    def fuel_type(self):
        return "Petrol And Deisel"
    def get_brand(self):
        return self.full_name() 
    def full_name(self):
        return f"{self.__model} by {self.__brand}" 
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__( brand , model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla , ElectricCar))   
#my_car = Car("Tata", "Safari")
#print(my_car.model)
print("Exit Successfully:")

#Multiple Inheritance
#Create two classes battery and engine , and let the ElectricCar class inherit from both, demonstrating
#Multiple inheritance

class Car:
    Total_car = 0

    def __init__(self ,brand , model):
        self.__brand = brand
        self.__model = model
        Car.Total_car +=1 
    def fuel_type(self):
        return "Petrol And Deisel"
    def get_brand(self):
        return self.full_name() 
    def full_name(self):
        return f"{self.__model} by {self.__brand}" 
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__( brand , model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
 
class Battery:
    def battery_info(self):
        return "this is battery"
    
class Engine:
    def engine_info(self):
        return "This is engine"
class ElectricCar2(Battery , Engine, Car):
    pass
my_new_tesla = ElectricCar2("tesla","model A")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
    
      