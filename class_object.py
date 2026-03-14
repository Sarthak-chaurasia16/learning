"""# 1. Basic Class and Object
class Car:
#python mein __init__ ka syntax hai aur ye constructor hai and self lagana hai jisse khud ko refer kar sake (Telephone line ko connect karne ke liye)
    def __init__(self ,brand , model):
        self.brand = brand
        self.model = model
my_car = Car("Toyota", "Corolla")
print(f"{my_car.model} By {my_car.brand} ")
my_new_car = Car("Tata", "Safari")
print(f"{my_new_car.model} By {my_new_car.brand}")

#2. Class Method and Self  
class Car:
    def __init__(self ,brand , model):
        self.brand = brand
        self.model = model 
    def full_name(self):
        return f"{self.model} by {self .brand} "
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model Y")
car3 = Car("Maruti Suzuki", "Sedan")
car4 = Car("Bentley", "Flying Spur")
my_car = [car1, car2, car3,car4]
print("------My New Car-------")
for my_new_car in my_car:
#Ab parenthesis lagayenge kuki ab attribute nhi hai function hai full name
    print(my_new_car.full_name())
exit
print("Exit Successfully:)")

#3. Inheritance 
class Car:
    def __init__(self ,brand , model):
        self.brand = brand
        self.model = model 
    def full_name(self):
        return f"{self.model} by {self .brand} "
#Inherit kia hai isliye parenthesis ke andar parent class ka name likhna padega warna directly class name likh dete
class ElectricCar(Car):
    
    #super() ka matlab hai derived class mein andar jo parent class ka name likha hai 
    #use access krke uss class mein jao fir uske andar __init__ function access kro aur 
    #usme brand aur model tha isliye iss wali mein brand and model likh denge 
    
    
    def __init__(self,brand, model, battery_size):
        super().__init__(brand , model)
        self.battery_size = battery_size
my_tesla = ElectricCar("Tesla", "Model S", "90KWh")
print(my_tesla.full_name())
exit
print("Exit Successfully:)")
#4. Encapsulation
class Car:
    #Attribute ke aage do underscore lagane se private ho jata hai like brand ke aage lagae hai
    # Ab usko access krne ke liye get method banana padega kuki woh car class mein access ho jayega 
    #but uska koi object bana kar access kroge toh access nhi hoga
    def __init__(self ,brand , model):
        self.__brand = brand
        self.model = model 
    def get_brand(self):
        return self.full_name() + "! "
    def full_name(self):
        return f"{self.model} by {self .__brand} "

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__( brand , model)
        self.battery_size = battery_size
my_tesla = ElectricCar("Tesla", "Model S", "90KWh")
#print(my_tesla.__brand)
print(my_tesla.get_brand())
exit
print("Exit Successfully:)")

#5. Polymorphism (Dono mein fuel type method same hai )
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

class ElectricCar(Car):
    def __init__(self,brand, model, battery_size):
        super().__init__( brand , model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    
Electric_1 = ElectricCar("Tesla", "Model S", "90KWh")
car1 = Car("Tata", "Safari")
car2 = Car("Bentley","Flying Spur")
print(f"{Electric_1.get_brand()} working by using {Electric_1.fuel_type()}")
print(f"{car1.get_brand()} working by using {car1.fuel_type()}")
print(f"{car2.get_brand()} working by using {car2.fuel_type()}")
exit
print("Exit Successfully:)")"""

