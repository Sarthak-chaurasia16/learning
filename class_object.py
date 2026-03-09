# 1. Basic Class and Object
"""class Car:
python mein __init__ ka syntax hai aur ye constructor hai and self lagana hai jisse khud ko refer kar sake (Telephone line ko connect karne ke liye)
    def __init__(self ,brand , model):
        self.brand = brand
        self.model = model
my_car = Car("Toyota", "Corolla")
print(f"{my_car.model} By {my_car.brand} ")
my_new_car = Car("Tata", "Safari")
print(f"{my_new_car.model} By {my_new_car.brand}")
"""
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

