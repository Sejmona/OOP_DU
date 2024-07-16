
# Definice základní třídy Device
class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
    
    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Power: {self.power}W"

# Třída CoffeeMachine dědící od Device
class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_capacity, coffee_type):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity 
        self.coffee_type = coffee_type  

    def make_coffee(self):
        return f"Making {self.coffee_type} coffee!"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Water Capacity: {self.water_capacity}L, Coffee Type: {self.coffee_type}"

# Třída Blender dědící od Device
class Blender(Device):
    def __init__(self, brand, model, power, capacity, speed_settings):
        super().__init__(brand, model, power)
        self.capacity = capacity 
        self.speed_settings = speed_settings  

    def blend(self):
        return "Blending at speed setting!"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Capacity: {self.capacity}L, Speed Settings: {self.speed_settings}"

# Třída MeatGrinder dědící od Device
class MeatGrinder(Device):
    def __init__(self, brand, model, power, material, max_capacity):
        super().__init__(brand, model, power)
        self.material = material  
        self.max_capacity = max_capacity  

    def grind_meat(self):
        return "Grinding meat!"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Material: {self.material}, Max Capacity: {self.max_capacity}kg"

# Testovací příklady
coffee_machine = CoffeeMachine("DeLonghi", "Magnifica", 1450, 1.8, "Espresso")
blender = Blender("Philips", "HR3652", 1400, 2.0, 5)
meat_grinder = MeatGrinder("Bosch", "MFW67440", 700, "Stainless Steel", 3.5)

# Výpis informací a volání metod
print(coffee_machine.get_info())
print(coffee_machine.make_coffee())

print(blender.get_info())
print(blender.blend())

print(meat_grinder.get_info())
print(meat_grinder.grind_meat())
