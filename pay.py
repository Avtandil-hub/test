# class Car:
#     owner = 'Avtandil'
#     make = 'Ford'
#     model = 'Raptor'
#     year = '2021'
#     odometer = 0
# ford = Car()

# class Airplane(Car):
#     make = 'USA Airplanes'
#     model = 'Boing 400-800'
#     year = '2018'
#     # odometer = 0

# boing = Airplane()

# print(boing.odometer)


#Инкапсуляция
class B:
    count = 0
    def __init__(self):
        B.count += 1
    def __del__(self):
        B.count -= 1
    def _end(self):
        print('end')
a = B()
print(a.count)
a._end()