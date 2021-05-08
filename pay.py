class Car:
    owner = 'Avtandil'
    make = 'Ford'
    model = 'Raptor'
    year = '2021'
    odometer = 0
ford = Car()

class Airplane(Car):
    make = 'USA Airplanes'
    model = 'Boing 400-800'
    year = '2018'
    # odometer = 0

boing = Airplane()

print(boing.odometer)