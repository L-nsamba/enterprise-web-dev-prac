class Car():
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

    def get_car_info(self):
        print(f"""
        Car Name: {self.name}
        Car Color: {self.color}
        Production Year: {self.year}
""")                    
        
class CarPerformance(Car): #Inheriting the Car Class
    def __init__(self, name, color, year, fuel_consumption, speed):
        super().__init__(name, color, year)
        self.fuel_consumption = fuel_consumption
        self.speed = speed

    def vehicle_performance(self):
        print(f"""
        Fuel Consumption: {self.fuel_consumption}
        Speed: {self.speed}
""")
        
car_one = CarPerformance("Toyota", "pink", 2025, "4.5L/60km", "180 km/hr")
car_one.get_car_info()
car_one.vehicle_performance()

car_two = CarPerformance("Honda", "blue-black", 2022, "6L/100km", "220 km/hr")
car_two.get_car_info()
car_two.vehicle_performance()