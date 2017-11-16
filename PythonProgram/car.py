class Car():
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer= 0
        self.gas = 10
    
    def get_descriptive_name(self):
        return '{} {} {}款'.format(self.year, self.maker, self.model)
    
    def update_odometer(self, mileage):
        if mileage > self.odometer:
            self.odometer = mileage
        else:
            print('you can not roll back the odometer')

    def fill_gas_tank(self, gas):
        self.gas = gas
    
    
class ElectricCar(Car):
    """电动汽车"""
    def __init__(self, maker, model, year):
        super().__init__(maker, model, year)
        self.battery_size = 70
    
    def get_battery_size(self):
        return self.battery_size

    def get_descriptive_name(self):
        return super().get_descriptive_name() + ', 新能源汽车.'